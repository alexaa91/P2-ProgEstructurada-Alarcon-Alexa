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
 # TODO: Implementar lógica
 pass
# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
 print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
 # TODO: Invocar las funciones, orquestar el flujo y mostrar reportes ordenados.
