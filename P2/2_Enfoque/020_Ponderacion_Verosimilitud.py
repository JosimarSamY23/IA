import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from os import system

# Parámetros de la distribución
true_mean = 5
true_std  = 2
num_samples = 500

# Generamos datos de una distribución normal
data = np.random.normal(true_mean, true_std, num_samples)

# Mostramos el histograma de los datos generados
system('cls')
plt.hist(data, bins=30, density=True, alpha=0.6, color='g')
plt.title('Datos Generados de una Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

def calcular_verosimilitud(data, mean, std):
    # Calcula la verosimilitud de los datos bajo la distribución normal
    return norm.pdf(data, mean, std)

# Estimamos media y desviación estándar iniciales
initial_mean = np.mean(data)
initial_std = np.std(data)

# Calculamos las verosimilitudes
likelihoods = calcular_verosimilitud(data, initial_mean, initial_std)

# Mostramos las verosimilitudes
print("Verosimilitudes (primeras 10):", likelihoods[:10])

def estimar_parametros(data, likelihoods):
    # Pondera las muestras según sus verosimilitudes
    weighted_mean = np.sum(data * likelihoods) / np.sum(likelihoods)
    weighted_variance = np.sum(likelihoods * (data - weighted_mean) ** 2) / np.sum(likelihoods)
    return weighted_mean, weighted_variance

# Estimamos los parámetros ponderados
weighted_mean, weighted_variance = estimar_parametros(data, likelihoods)

print(f"\nMedia Ponderada Estimada   : {weighted_mean:.4f}")
print(f"Varianza Ponderada Estimada: {weighted_variance:.4f}")
