# Guía IV - Soluciones Completas

Modelación Matemática Fundamental
Profesor: Jorge Antonio Becerril Gómez
Tecnológico de Monterrey
Temas: Integración por Partes, Fracciones Parciales

# Integración por Partes

Fórmula: $$\int u \, dv = uv - \int v \, du$$

1. Problema: $$\int x^2 \cos(2x) \, dx$$

Solución:
Elige $u = x^2$ (polinomio) y $dv = \cos(2x)dx$ (trigonométrica). Recuerda la prioridad ILATE.
Primera aplicación de integración por partes
$$u = x^2 \quad \Rightarrow \quad du = 2x \, dx$$
$$dv = \cos(2x) \, dx \quad \Rightarrow \quad v = \frac{1}{2}\sin(2x)$$
$$\int x^2 \cos(2x) \, dx = \frac{1}{2}x^2 \sin(2x) - \int x\sin(2x) \, dx$$
Segunda aplicación de integración por partes en $\int x\sin(2x) \, dx$
$$u = x \quad \Rightarrow \quad du = dx$$
$$dv = \sin(2x) \, dx \quad \Rightarrow \quad v = -\frac{1}{2}\cos(2x)$$
$$\int x\sin(2x) \, dx = -\frac{1}{2}x\cos(2x) + \frac{1}{4}\sin(2x)$$
Combinando resultados
$$\int x^2 \cos(2x) \, dx = \frac{1}{2}x^2 \sin(2x) + \frac{1}{2}x\cos(2x) - \frac{1}{4}\sin(2x) + C$$
Respuesta final: $$\frac{1}{2}x^2 \sin(2x) + \frac{1}{2}x\cos(2x) - \frac{1}{4}\sin(2x) + C$$

2. Problema: $$\int x^2 e^{-2x} \, dx$$

Solución:
Polinomio por exponencial: usa $u = x^2$, $dv = e^{-2x}dx$. Necesitarás aplicar integración por partes dos veces.
Primera aplicación
$$u = x^2 \quad \Rightarrow \quad du = 2x \, dx$$
$$dv = e^{-2x} \, dx \quad \Rightarrow \quad v = -\frac{1}{2}e^{-2x}$$
$$\int x^2 e^{-2x} \, dx = -\frac{1}{2}x^2 e^{-2x} + \int x e^{-2x} \, dx$$
Segunda aplicación en $\int x e^{-2x} \, dx$
$$u = x \quad \Rightarrow \quad du = dx$$
$$dv = e^{-2x} \, dx \quad \Rightarrow \quad v = -\frac{1}{2}e^{-2x}$$
$$\int x e^{-2x} \, dx = -\frac{1}{2}x e^{-2x} - \frac{1}{4}e^{-2x}$$
Combinando resultados
$$\int x^2 e^{-2x} \, dx = -\frac{1}{4}e^{-2x}(2x^2 + 2x + 1) + C$$
Respuesta final: $$-\frac{1}{4}e^{-2x}(2x^2 + 2x + 1) + C$$

3. Problema: $$\int x^2 \ln(2x) \, dx$$

Solución:
Las funciones logarítmicas siempre deben elegirse como $u$ en ILATE. ¿Qué debería ser $dv$?
Configurar integración por partes
$$u = \ln(2x) \quad \Rightarrow \quad du = \frac{1}{x} \, dx$$
$$dv = x^2 \, dx \quad \Rightarrow \quad v = \frac{x^3}{3}$$
Aplicar la fórmula
$$\int x^2 \ln(2x) \, dx = \frac{x^3}{3}\ln(2x) - \frac{x^3}{9} + C$$
Respuesta final: $$\frac{x^3}{3}\ln(2x) - \frac{x^3}{9} + C$$

4. Problema: $$\int x e^{-\frac{x}{2}} \, dx$$

Solución:
Esto requiere solo una aplicación de integración por partes. Elige $u = x$.
Configuración
$$u = x \quad \Rightarrow \quad du = dx$$
$$dv = e^{-\frac{x}{2}} \, dx \quad \Rightarrow \quad v = -2e^{-\frac{x}{2}}$$
Aplicar la fórmula
$$\int x e^{-\frac{x}{2}} \, dx = -2e^{-\frac{x}{2}}(x + 2) + C$$
Respuesta final: $$-2(x+2)e^{-\frac{x}{2}} + C$$

5. Problema: $$\int x^2 \sin(x) \, dx$$

Solución:
Similar al problema 1. Aplica integración por partes dos veces.
Primera aplicación
$$u = x^2 \quad \Rightarrow \quad du = 2x \, dx$$
$$dv = \sin(x) \, dx \quad \Rightarrow \quad v = -\cos(x)$$
$$\int x^2 \sin(x) \, dx = -x^2 \cos(x) + 2\int x\cos(x) \, dx$$
Segunda aplicación en $\int x\cos(x) \, dx$
$$\int x\cos(x) \, dx = x \sin(x) + \cos(x)$$
Combinando resultados
$$\int x^2 \sin(x) \, dx = -x^2 \cos(x) + 2x \sin(x) + 2\cos(x) + C$$
Respuesta final: $$-x^2 \cos(x) + 2x \sin(x) + 2\cos(x) + C$$

6. Problema: $$\int e^x \sin(x) \, dx$$

Solución:
Este es un caso especial. Usa integración por partes dos veces y resuelve algebraicamente.
Sustituyendo de vuelta y resolviendo para la integral
$$\int e^x \sin(x) \, dx = \frac{e^x(\sin(x) - \cos(x))}{2} + C$$
Respuesta final: $$\frac{e^x(\sin(x) - \cos(x))}{2} + C$$

7. Problema: $$\int \arcsin(x) \, dx$$

Solución:
Cuando integras funciones inversas solas, usa $u = \arcsin(x)$ y $dv = dx$.
Respuesta final
$$\int \arcsin(x) \, dx = x\arcsin(x) + \sqrt{1-x^2} + C$$
Respuesta final: $$x\arcsin(x) + \sqrt{1-x^2} + C$$

8. Problema: $$\int_0^1 x \sin(2x) \, dx$$

Solución:
Primero encuentra la antiderivada usando integración por partes, luego evalúa en los límites.
Encontrar antiderivada
$$\int x \sin(2x) \, dx = -\frac{1}{2}x\cos(2x) + \frac{1}{4}\sin(2x)$$
Evaluar integral definida
$$\int_0^1 x \sin(2x) \, dx = \frac{1}{4}\sin(2) - \frac{1}{2}\cos(2)$$
Respuesta final: $$\frac{1}{4}\sin(2) - \frac{1}{2}\cos(2)$$

# Integración con Fracciones Parciales

9. Problema: $$\int \frac{1}{x^2 + x - 2} \, dx$$

Solución:
Primero factoriza el denominador, luego descompone en fracciones parciales con factores lineales.
Integrar
$$\int \frac{1}{x^2 + x - 2} \, dx = \frac{1}{3}\ln\left|\frac{x-1}{x+2}\right| + C$$
Respuesta final: $$\frac{1}{3}\ln\left|\frac{x-1}{x+2}\right| + C$$

10. Problema: $$\int \frac{1}{x^3(1-x)} \, dx$$

Solución:
El factor $x^3$ es un factor lineal repetido. Necesitas tres términos para él en la descomposición en fracciones parciales.
Integrar
$$\int \frac{1}{x^3(1-x)} \, dx = \ln\left|\frac{x}{1-x}\right| - \frac{1}{x} - \frac{1}{2x^2} + C$$
Respuesta final: $$\ln\left|\frac{x}{1-x}\right| - \frac{1}{x} - \frac{1}{2x^2} + C$$

11. Problema: $$\int \frac{x^2 + 1}{x^2 - 1} \, dx$$

Solución:
El grado del numerador es igual al grado del denominador. ¿Qué debes hacer primero? (División polinomial).
Integrar
$$\int \frac{x^2 + 1}{x^2 - 1} \, dx = x + \ln\left|\frac{x-1}{x+1}\right| + C$$
Respuesta final: $$x + \ln\left|\frac{x-1}{x+1}\right| + C$$

12. Problema: $$\int \frac{x^2 - 2}{x(x^2 + 2)} \, dx$$

Solución:
Tienes un factor lineal ($x$) y un factor cuadrático irreducible ($x^2 + 2$). Usa las formas apropiadas para cada uno.
Respuesta final
$$\int \frac{x^2 - 2}{x(x^2 + 2)} \, dx = \ln\left|\frac{x^2 + 2}{x}\right| + C$$
Respuesta final: $$\ln\left|\frac{x^2 + 2}{x}\right| + C$$

13. Problema: $$\int \frac{3x + 5}{x^2 - x - 2} \, dx$$

Solución:
Factoriza el denominador primero, luego usa fracciones parciales con dos factores lineales.
Integrar
$$\int \frac{3x + 5}{x^2 - x - 2} \, dx = \frac{11}{3}\ln|x-2| - \frac{2}{3}\ln|x+1| + C$$
Respuesta final: $$\frac{11}{3}\ln|x-2| - \frac{2}{3}\ln|x+1| + C$$

14. Problema: $$\int \frac{2x^2 + 3x + 1}{(x-1)(x^2+4)} \, dx$$

Solución:
Factores mixtos: uno lineal, uno cuadrático irreducible. Configura las fracciones parciales en consecuencia.
Combinar resultados
$$\int \frac{2x^2 + 3x + 1}{(x-1)(x^2+4)} \, dx = \frac{6}{5}\ln|x-1| + \frac{2}{5}\ln(x^2+4) + \frac{19}{10}\arctan\left(\frac{x}{2}\right) + C$$
Respuesta final: $$\frac{6}{5}\ln|x-1| + \frac{2}{5}\ln(x^2+4) + \frac{19}{10}\arctan\left(\frac{x}{2}\right) + C$$

15. Problema: $$\int \frac{\sec^2 x}{\tan^2 x+3\tan x+2} \, dx$$

Solución:
Esto parece complicado, pero observa que $\frac{d}{dx}[\tan x] = \sec^2 x$. ¡Intenta una sustitución!
Sustituir de vuelta
$$\int \frac{\sec^2 x}{\tan^2 x+3\tan x+2} \, dx = \ln\left|\frac{\tan x+1}{\tan x+2}\right| + C$$
Respuesta final: $$\ln\left|\frac{\tan x+1}{\tan x+2}\right| + C$$

# Directivas para el Chatbot Tutor

Instrucciones para el chatbot tutor:

* Nunca proporcionar la respuesta final inmediatamente - Guiar a los estudiantes a través del proceso de resolución con pistas y preguntas.
* Diagnosticar dónde está atascado el estudiante - Hacer preguntas aclaratorias para identificar su dificultad específica (elegir $u$ y $dv$, álgebra, técnica de integración, etc.).
* Proporcionar pistas dirigidas, no soluciones - Sugerir qué técnica usar, recordar fórmulas o señalar ejemplos similares sin resolver los pasos.
* Comentar el trabajo del estudiante - Pedirles que muestren su intento, luego guiarlos para encontrar sus propios errores o continuar desde donde se detuvieron.
*  Usar las soluciones solo como referencia - Verificar el trabajo del estudiante contra estas soluciones, pero revelar pasos progresivamente y solo cuando el estudiante esté verdaderamente atascado.
* Pasos clave para la descomposición en fracciones parciales:
  * Verificar si el grado del numerador $<$ grado del denominador. Si no, realizar división polinomial primero.
  * Factorizar el denominador completamente.
  * Configurar la forma de fracciones parciales basada en los factores.
  * Resolver para las constantes usando varios métodos (cubrir, sustitución, comparar coeficientes).
  * Integrar término por término.
