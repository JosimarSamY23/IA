import numpy as np
import matplotlib.pyplot as plt
from os import system

def muestreo_por_rechazo(num_samples):
    samples = []
    accepted_samples = 0

    while accepted_samples < num_samples:
        # Muestreo de la distribución de propuesta (distribución normal)
        x = np.random.normal(0.5, 0.1)  # media 0.5, desviación estándar 0.1
        if 0 <= x <= 1:  # Asegurarse de que x está en el intervalo [0, 1]
            # Muestreo de la función de densidad de la distribución objetivo
            # Para la U(0, 1), la densidad es constante (1) en el intervalo
            # y la altura de la normal se evalúa en x
            y = np.random.uniform(0, 1)
            if y < (1 / (0.1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 0.5) / 0.1) ** 2):
                samples.append(x)
                accepted_samples += 1

    return samples

# Realizar el muestreo por rechazo
num_samples = 500
muestras_rechazo = muestreo_por_rechazo(num_samples)

# Mostrar resultados
system('cls')
plt.hist(muestras_rechazo, bins=30, density=True, alpha=0.6, color='g')
plt.title('Muestreo por Rechazo de U(0, 1)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

