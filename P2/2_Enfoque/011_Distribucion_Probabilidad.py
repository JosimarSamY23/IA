import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from os import system

def generar_datos_distribucion_normal(media, desviacion_estandar, num_datos):
    #Genera una muestra de datos a partir de una distribución normal.

    datos = np.random.normal(media, desviacion_estandar, num_datos)
    return datos

def graficar_distribucion(datos):   #Grafica la distribución de los datos generados.
    plt.figure(figsize=(8, 6))
    sns.histplot(datos, kde=True, color='blue', bins=30)
    plt.title('Distribución Normal')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

# Parámetros de la distribución normal
media = 0               # Media de la distribución
desviacion_estandar = 1 # Desviación estándar
num_datos = 500         # Número de datos a generar

# Generar datos de una distribución normal
datos = generar_datos_distribucion_normal(media, desviacion_estandar, num_datos)

# Graficar la distribución
system('cls')
graficar_distribucion(datos)
