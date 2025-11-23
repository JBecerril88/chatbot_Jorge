import os
import streamlit as st
from dotenv import load_dotenv

# --- LangChain/LangGraph/Herramientas ---
from typing import Annotated, Sequence, List
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph.message import add_messages
from langgraph.graph import END, StateGraph, START
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# --- Modelos y Embeddings (Google Gemini) ---
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.document_loaders import TextLoader # Usamos TextLoader para el Markdown limpio

# --- Templates de Streamlit (Asumo que tienes este archivo) ---
# from htmlTemplates import css, bot_template, user_template 
# Si no tienes htmlTemplates.py, reemplaza esto con mensajes simples de st.chat_message

# Cargar variables de entorno
load_dotenv()

# --- Configuración de Modelos y Embeddings ---
# Usamos las variables de entorno
# api_key = os.getenv('GROQ_API_KEY') # No se usa, pero se mantiene para referencia
google_key = os.getenv('GOOGLE_API_KEY')

# Modelos
# Usa un modelo consistente para el LLM y un modelo consistente para los embeddings
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash") 
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") 

# --- FUNCIÓN DE CARGA DE BASE DE DATOS (RAG) ---

def load_db(embeddings, path: str):
    """
    Carga el contenido del archivo Markdown limpio, lo divide en chunks y crea un vectorstore FAISS.
    """
    try:
        # 1. Cargar el archivo .md usando TextLoader (ideal para texto plano/Markdown)
        loader = TextLoader(path, encoding="utf8")
        documents = loader.load()

        # 2. Inicializar el segmentador de texto
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=150,
            # Separadores ajustados para Markdown limpio
            separators=["\n\n", "\n", " "] 
        )
        
        # 3. Dividir los documentos en chunks
        texts = text_splitter.split_documents(documents)

        # 4. Crear el Vectorstore FAISS
        vectorstore = FAISS.from_documents(texts, embeddings)
        st.success(f"Base de datos de {len(texts)} chunks creada exitosamente.")
        return vectorstore
        
    except Exception as e:
        st.error(f"Error al cargar o crear la base de datos: {e}")
        st.info("Asegúrate de que el archivo 'guia_calculo_plana.md' existe y el contenido está limpio (sin caracteres complejos de LaTeX).")
        return None

# --- STREAMLIT: GESTIÓN DE ESTADO Y CARGA ÚNICA ---

# Inicializar historial de chat y base de datos
if 'chat_history_display' not in st.session_state:
    st.session_state.chat_history_display = []
if 'vectorstore' not in st.session_state:
    st.write("Cargando o creando la base de datos vectorial...")
    FAISS_INDEX_PATH = "faiss_index"
    DOCUMENT_PATH = 'guia_calculo_plana.md' # <- Nombre del archivo limpio

    if os.path.exists(FAISS_INDEX_PATH):
        try:
            # Carga la BD existente
            st.session_state.vectorstore = FAISS.load_local(
                FAISS_INDEX_PATH,
                embeddings=embeddings,
                allow_dangerous_deserialization=True
            )
            st.success("Base de datos cargada desde el índice 'faiss_index'.")
        except Exception as e:
            st.error(f"Error al cargar la BD de FAISS: {e}")
            st.session_state.vectorstore = None
    else:
        # Crea la BD y la guarda
        st.session_state.vectorstore = load_db(embeddings, DOCUMENT_PATH)
        if st.session_state.vectorstore:
            st.session_state.vectorstore.save_local(FAISS_INDEX_PATH)
            st.success("Base de datos creada y guardada.")


# Si la base de datos se cargó correctamente, configurar el retriever
if st.session_state.vectorstore:
    retriever = st.session_state.vectorstore.as_retriever()

    # --- CADENAS DE RAG CON HISTORIAL (HISTORY AWARE RETRIEVER) ---

    # 1. Contextualizador de Preguntas
    contextualize_q_system_prompt = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

    # 2. Prompt del Chatbot Tutor
    system_prompt2 = (
        "Este documento contiene informacion para ayudar a los estudiantes con la solución a su guia de integrales."
        "Tu objetivo es guiar a los estudiantes paso a paso sin darles las respuestas completas directamente."
        "Cuando un estudiante te haga una pregunta: identifica en que paso especıfico esta trabajando, proporciona ayuda para ese paso particular usando la informacion de este documento."  
        "Usa las directivas de ayuda que se describe al inicio del archivo (No dar la respuesta final, diagnosticar, dar pistas dirigidas)."
        "Anima al estudiante a pensar y construir la solucion por sı mismo."
        "Si un estudiante esta completamente perdido, y ya le diste 4 sugerencias o mas, puedes mostrar un paso especıfico y pedirle que intente el siguiente. Contesta siempre en español."
        "\n\n"
        "Documento de Contexto: {context}"
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt2),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # 3. Cadena de RAG Completa
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    # --- LANGGRAPH ---

    class State(TypedDict):
        input: str
        chat_history: Annotated[Sequence[BaseMessage], add_messages]
        context: str
        answer: str

    def call_model(state: State):
        # La cadena rag_chain requiere 'input' y 'chat_history'
        response = rag_chain.invoke({"input": state["input"], "chat_history": state["chat_history"]})
        
        # Devuelve el nuevo par de mensajes para actualizar el historial de LangGraph
        return {
            "chat_history": [
                HumanMessage(state["input"]),
                AIMessage(response["answer"]),
            ],
            "context": response["context"],
            "answer": response["answer"],
        }

    # Definición y compilación del grafo
    workflow = StateGraph(state_schema=State)
    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)
    
    # --- STREAMLIT UI ---

    st.header('Chatbot MA1028 - Guía Integración')

    # Mensaje inicial
    if not st.session_state.chat_history_display:
        st.write("Hola, soy tu tutor de cálculo, ¿en qué problema de la guía te puedo ayudar?")

    question = st.chat_input("Escribe tu pregunta o tu avance en el problema.")
    
    # Manejar el input del usuario
    if question:
        # 1. Configuración de LangGraph (Thread ID único para la sesión)
        config = {"configurable": {"user_id": "1", "thread_id": "1"}} 
        
        # 2. Invocar el grafo con el historial acumulado
        # LangGraph recupera y gestiona el historial automáticamente gracias al checkpointer (memory)
        # Solo necesitamos darle el input y el historial almacenado
        
        # Reconstruye el historial a partir de los mensajes mostrados (Human/AI)
        langgraph_history = [
            m for m in st.session_state.chat_history_display if isinstance(m, (HumanMessage, AIMessage))
        ]
        
        result = app.invoke({"input": question, "chat_history": langgraph_history}, config)
        
        # 3. Actualizar el historial de Streamlit para la visualización
        # El historial de visualización se actualiza con el último par H/A
        st.session_state.chat_history_display.extend([
            HumanMessage(content=question),
            AIMessage(content=result['answer'])
        ])

    # 4. Mostrar todo el historial
    save_chat = ""
    for message in st.session_state.chat_history_display:
        save_chat += f"[{'Tú' if isinstance(message, HumanMessage) else 'Bot'}]: {message.content}\n"
        
        # Mostrar usando la estructura de chat de Streamlit (o tus templates)
        with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
            st.markdown(message.content)
            
    # Botón de descarga
    st.download_button("Descargar chat", save_chat, file_name="chat_tutor.txt")

else:
    # Mensaje si la base de datos falló
    st.error("El chatbot no puede iniciar porque la base de datos no se pudo cargar o crear. Revisa la consola para ver los errores de `load_db`.")
