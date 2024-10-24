import numpy as np
import matplotlib.pyplot as plt
from os import system

# Definimos la distribución objetivo (una normal)
def target_distribution(x):
    return (1/np.sqrt(2 * np.pi)) * np.exp(-0.5 * (x - 2)**2)

# Visualizar la distribución objetivo
x = np.linspace(-3, 7, 100)
y = target_distribution(x)
plt.plot(x, y, label='Distribución Objetivo')
plt.title('Distribución Normal Objetivo')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.grid()
plt.show()

def metropolis_hastings(num_samples, proposal_std):
    # Inicializamos la cadena
    samples = []
    current_sample = 0  # punto de partida

    for _ in range(num_samples):
        # Proponer un nuevo punto
        proposed_sample = np.random.normal(current_sample, proposal_std)

        # Calcular la razón de aceptación
        acceptance_ratio = target_distribution(proposed_sample) / target_distribution(current_sample)

        # Aceptar o rechazar la nueva muestra
        if np.random.rand() < acceptance_ratio:
            current_sample = proposed_sample
        
        samples.append(current_sample)

    return np.array(samples)

# Generar muestras usando Metropolis-Hastings
num_samples = 800
proposal_std = 1.0  # desviación estándar de la propuesta
samples = metropolis_hastings(num_samples, proposal_std)

# Visualizar las muestras
system('cls')
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Muestras MCMC')
plt.plot(x, y, label='Distribución Objetivo', color='red')
plt.title('Muestras de Monte Carlo para Cadenas de Markov')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.grid()
plt.show()