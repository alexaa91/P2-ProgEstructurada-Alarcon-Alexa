"""
Nombre del Alumno: Alexa Guadalupe Alarcón González
Matrícula: UX25II114
Fecha: 25 de mayo de 2026
Examen Segundo Parcial - Programación Estructurada
"""
# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================
import datetime
import math
import random
import statistics
import sys
# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================
MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95
# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================
def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
    """
 
    sistema_operativo = sys.platform
    version_python = sys.version
    ruta_interprete = sys.executable

    print(f"\nSistema Operativo: {sistema_operativo}")
    print(f"\nVersión de Python: {version_python}")
    print(f"\nRuta del Intérprete: {ruta_interprete}")

    version_mayor = sys.version_info[0]
    version_menor = sys.version_info[1]
    if version_mayor < 3 or (version_mayor == 3 and version_menor < 8):
        print("ADVERTENCIA: Se recomienda Python 3.8 o superior.")
    else:
        print(f"Compatibilidad: OK (Python {version_mayor}.{version_menor})")


def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
    Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'.
    """
    
    inicio_simulacion = datetime.datetime.now()
    fecha_formateada = inicio_simulacion.strftime("%d/%m/%Y %H:%M:%S")
    print(f"\nInicio: {fecha_formateada}")
 
    lista_loss = []
    lista_latencia = []
    eventos_log = ["Epoch exitoso", "Gradiente inestable", "Actualización de pesos"]
 
    contador_epoch = 1
    while contador_epoch <= cantidad_epochs:
        loss_epoch = random.uniform(0.05, 1.0)
        probabilidad = random.random()
        evento = random.choice(eventos_log)
 
        lista_loss.append(loss_epoch)
        lista_latencia.append(random.uniform(50, 300)) 
        if probabilidad >= 0.3:
            estado = "OK"
        else:
            estado = "FALLO"
        print(f"Epoch {contador_epoch} -> Loss: {loss_epoch:.2f} | {estado} | {evento}")
        contador_epoch = contador_epoch + 1
 
    fin_simulacion = datetime.datetime.now()
    duracion = fin_simulacion - inicio_simulacion
 
    print(f"Fin: {fin_simulacion.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Duración: {duracion.total_seconds():.2f} segundos")
 
    return lista_loss, lista_latencia


def analizar_rendimiento(lista_loss):
    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
    """
    print("\n=== ANÁLISIS ESTADÍSTICO DE RENDIMIENTO ===")
    if len(lista_loss) < 2:
        print("Error: No hay suficientes datos para un análisis estadístico completo.")
    
        if len(lista_loss) == 1:
            print(f"Media única: {statistics.mean(lista_loss):.4f}")
        return

    media_loss = statistics.mean(lista_loss)
    desviacion_loss = statistics.stdev(lista_loss)
    mediana_loss = statistics.median(lista_loss)
    
    print(f"Media del Loss: {media_loss:.4f}")
    print(f"Desviación Estándar (Estabilidad): {desviacion_loss:.4f}")
    print(f"Mediana del Loss: {mediana_loss:.4f}")


def calcular_rmse(predicciones, reales):
    """
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
    Requisitos: 3 llamadas distintas a la biblioteca 'math'.
    """
    suma_errores = 0.0
    total_elementos = len(predicciones)
    
    if total_elementos == 0:
        return 0.0

    for i in range(total_elementos):
        diferencia = predicciones[i] - reales[i]
        suma_errores += math.pow(diferencia, 2)
        
    promedio_errores = suma_errores / total_elementos
    rmse = math.sqrt(promedio_errores)
    error_absoluto_final = math.fabs(rmse)
    
    return error_absoluto_final
 


# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
    # 1. Información del sistema
    print("\n1. Validación del Entorno")
    obtener_info_sistema()
    
    # 2. Simulación de entrenamiento
    print("\n2. Simulación de Épocas")
    # Capturamos los dos valores que retorna tu función (lista_loss y lista_latencia)
    perdidas, latencias = simular_metricas_entrenamiento(MAX_EPOCHS)
    # 3. Análisis estadístico de rendimiento
    # Pasamos la lista de pérdidas como lo requiere la función
    analizar_rendimiento(perdidas)
    print("\nCÁLCULO DE ERROR DE PRECISIÓN")
    valores_ideales = [0.0] * len(perdidas)
    rmse_resultado = calcular_rmse(perdidas, valores_ideales)
    print(f"Resultado RMSE del Modelo: {rmse_resultado:.4f}")
    
    print("\n3. Verificación de Seguridad del Sistema")
    ultima_perdida = perdidas[-1] 
    if ultima_perdida > UMBRAL_ERROR_CRITICO:
        print(f"[ALERTA CRÍTICA] La última pérdida ({ultima_perdida:.2f}) superó el umbral permitido ({UMBRAL_ERROR_CRITICO}).")
        print("Forzando salida limpia del sistema...")
        sys.exit(1)
    else:
        print(f"Estado del modelo estable. Último loss ({ultima_perdida:.2f}) bajo el umbral.")
        print("\n=== SIMULACIÓN FINALIZADA CON ÉXITO ===")
 
"""
1. En tu código, al usar datetime.datetime.now(),
¿cuál es el objeto/clase y cuál es el método que estás llamando? Explica
cómo se relaciona esto con el concepto de biblioteca externa.  
    Al invocar datetime.datetime.now(), el primer término hace referencia al módulo importado, el 
    segundo corresponde a la clase que define la estructura de fecha y hora en Python y now() es 
    el método encargado de consultar el reloj del sistema operativo para devolver un objeto con la hora 
    actual exacta, y esto se relaciona directamente con el concepto de biblioteca externa, ya que reutilizamos 
    código previamente desarrollado y optimizado, evitando tener que programar desde cero un 
    sistema que calcule milisegundos y los convierta manualmente en un formato de calendario


2. ¿Qué diferencia existe en la sintaxis de tu código
al importar un módulo completo (ej: import math) versus importar un método
específico (ej: from math import sqrt) al momento de invocar sus funciones?
    Cuando se utiliza la importación completa (import math), es necesario anteponer
    el nombre del módulo en cada llamada, por ejemplo math.sqrt(), lo que ayuda a evitar 
    conflictos entre funciones con nombres similares. En cambio, al importar una función 
    específica (from math import sqrt), esta se carga directamente en el entorno global y 
    puede utilizarse únicamente con su nombre, como sqrt()


3. Describe brevemente la secuencia lógica de pasos que
implementaste para conectar los datos generados por tu función de
simulación con la función que calcula el error (RMSE).
    La secuencia lógica comenzó en la función de simulación, la cual registró iterativamente 
    los valores flotantes del loss dentro de una colección dinámica y los retornó al bloque 
    principal bajo la variable perdidas, luego en el __main__ se generó una lista 
    espejo del mismo tamaño llamada valores_ideales llena solo de ceros (0.0) para 
    representar el escenario de convergencia perfecta del modelo, y finalmente ambas colecciones se inyectaron de forma ordenada como argumentos en la función calcular_rmse, 
    permitiendo que su bucle interno procesara las diferencias e índices correspondientes 
    para determinar el error cuadrático medio


4. Identifica al menos dos tipos de datos
complejos (colecciones) que utilizaste para organizar los resultados de tus
análisis y justifica por qué elegiste esa estructura en lugar de variables
simples
    Para la organización de los análisis se utilizaron listas (list) como estructuras de 
    almacenamiento de datos, ya que ofrecen una mayor flexibilidad en comparación con 
    variables simples como int o float, mientras que una variable convencional solo puede 
    contener un valor a la vez, una lista permite almacenar múltiples datos de forma 
    secuencial bajo un mismo identificador. Esto evitó tener que crear variables 
    independientes, haciendo que el código fuera más limpio, 
    escalable y eficiente

5. Al utilizar las funciones de la biblioteca
statistics, ¿tuviste que programar la fórmula matemática matemática de la
desviación estándar? Relaciona esto con el concepto de Abstracción visto
en clase.
    En ningún momento del desarrollo fue necesario programar manualmente la ecuación 
    matemática de la desviación estándar, la cual implica calcular la media de los datos, 
    restar cada elemento individual, elevar las diferencias al cuadrado, sumarlas, dividir 
    el resultado y finalmente extraer la raíz cuadrada. Esto representa claramente el 
    concepto de abstracción visto en clase, ya que la función statistics.stdev() actúa como 
    una “caja negra” que oculta toda la complejidad de su implementación interna
"""