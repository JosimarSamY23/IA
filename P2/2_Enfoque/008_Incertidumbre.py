import numpy as np
import matplotlib.pyplot as plt
from os import system

def lanzar_dado(num_lanzamientos): #Simula el lanzamiento de un dado de seis caras un número determinado de veces.
    resultados = np.random.randint(1, 7, size=num_lanzamientos)  # Lanzamiento de un dado
    return resultados

def calcular_probabilidades(resultados): #Calcula las probabilidades de obtener cada número en los resultados del dado.
    total_lanzamientos = len(resultados)
    probabilidades = {i: (np.sum(resultados == i) / total_lanzamientos) for i in range(1, 7)}

    return probabilidades

def calcular_estadisticas(resultados): #Calcula la media y varianza de los resultados.
    media = np.mean(resultados)
    varianza = np.var(resultados)

    return media, varianza

num_lanzamientos = 50
resultados      = lanzar_dado(num_lanzamientos)         # Simular lanzamientos de dado
probabilidades  = calcular_probabilidades(resultados)   # Calcular probabilidades
media, varianza = calcular_estadisticas(resultados)     # Calcular estadísticas

# Mostrar resultados
system('cls')
print("Resultados de lanzamientos:", resultados)
print("Probabilidades:", probabilidades)
print("Media:", media)
print("Varianza:", varianza)

# Graficar los resultados
plt.hist(resultados, bins=np.arange(1, 8) - 0.5, density=True, alpha=0.6, color='g', edgecolor='black')
plt.xticks(range(1, 7))
plt.xlabel('Número en el dado')
plt.ylabel('Frecuencia relativa')
plt.title('Distribución de resultados de lanzamientos de dado')
plt.grid(axis='y', alpha=0.75)
plt.show()