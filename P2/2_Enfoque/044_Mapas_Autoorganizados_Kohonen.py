import numpy as np
import matplotlib.pyplot as plt
from os import system

# Función para inicializar los pesos
def initialize_weights(num_neurons, input_dim):
    return np.random.rand(num_neurons, input_dim)

# Función para encontrar la neurona ganadora
def find_winner(weights, sample):
    distances = np.linalg.norm(weights - sample, axis=1)
    return np.argmin(distances)

# Función para actualizar pesos
def update_weights(weights, sample, winner_index, learning_rate, radius):
    for i in range(weights.shape[0]):
        distance = np.linalg.norm(weights[winner_index] - weights[i])
        if distance < radius:
            influence = np.exp(-distance / (2 * (radius ** 2)))
            weights[i] += learning_rate * influence * (sample - weights[i])

# Mapa autoorganizado de Kohonen
def kohonen_som(data, num_neurons, num_epochs, learning_rate_initial, radius_initial):
    input_dim = data.shape[1]
    weights = initialize_weights(num_neurons, input_dim)
    
    for epoch in range(num_epochs):
        learning_rate = learning_rate_initial * (1 - epoch / num_epochs)
        radius = radius_initial * (1 - epoch / num_epochs)
        
        for sample in data:
            winner_index = find_winner(weights, sample)
            update_weights(weights, sample, winner_index, learning_rate, radius)
    
    return weights

# Generar datos de ejemplo
data = np.random.rand(100, 2)  # 100 muestras, 2 dimensiones

# Parámetros del SOM
num_neurons = 10  # Número de neuronas
num_epochs = 50  # Número de épocas
learning_rate_initial = 0.1
radius_initial = 3

# Entrenar el SOM
weights = kohonen_som(data, num_neurons, num_epochs, learning_rate_initial, radius_initial)

# Visualizar los pesos del SOM
system('cls')
plt.scatter(weights[:, 0], weights[:, 1], marker='o', color='red', label='Neuronas')
plt.scatter(data[:, 0], data[:, 1], marker='x', color='blue', label='Datos')
plt.title('Mapa Autoorganizado de Kohonen')
plt.xlabel('Dimensión 1')
plt.ylabel('Dimensión 2')
plt.legend()
plt.show()
