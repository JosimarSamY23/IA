import numpy as np
import matplotlib.pyplot as plt
from os import system

# Parámetros del modelo AR(1)
phi = 0.8       # Coeficiente de autoregresión
sigma = 1       # Desviación estándar del ruido blanco
num_steps = 100 # Número de pasos en la simulación

# Inicialización
X = np.zeros(num_steps)
epsilon = np.random.normal(0, sigma, num_steps)  # Ruido blanco

# Simulación del proceso AR(1)
for t in range(1, num_steps):
    X[t] = phi * X[t-1] + epsilon[t]

# Gráfico de la serie temporal
system('cls')
plt.plot(X, label='Proceso AR(1)')
plt.title('Simulación de un Proceso Estacionario AR(1)')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()
plt.show()

# Función para calcular la autocorrelación
def autocorrelacion(x, lag):
    n = len(x)
    mean_x = np.mean(x)
    autocorr = np.sum((x[:n-lag] - mean_x) * (x[lag:] - mean_x)) / np.sum((x - mean_x)**2)
    return autocorr

# Calcula la autocorrelación para diferentes desfases (lags)
lags = 20  # Número de lags que queremos calcular
autocorrelaciones = [autocorrelacion(X, lag) for lag in range(1, lags + 1)]

# Gráfico de la autocorrelación
plt.bar(range(1, lags + 1), autocorrelaciones)
plt.xlabel('Lag')
plt.ylabel('Autocorrelación')
plt.title('Función de Autocorrelación del Proceso AR(1)')
plt.grid(True)
plt.show()
