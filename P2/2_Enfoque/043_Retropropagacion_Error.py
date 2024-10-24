import numpy as np
from os import system

# Función sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada y salida
X = np.array([[0, 0],
            [0, 1],
            [1, 0],
            [1, 1]])

y = np.array([[0], [1], [1], [0]])  # XOR

# Inicialización de pesos
np.random.seed(42)
weights = np.random.rand(2, 1)  # 2 entradas, 1 salida

# Parámetros
learning_rate = 0.1
epochs = 1000

# Entrenamiento de la red
for epoch in range(epochs):
    # Propagación hacia adelante
    input_layer = X
    predictions = sigmoid(np.dot(input_layer, weights))

    # Cálculo del error
    error = y - predictions

    # Retropropagación
    adjustments = error * sigmoid_derivative(predictions)
    weights += np.dot(input_layer.T, adjustments) * learning_rate

# Resultados
system('cls')
print("Pesos después del entrenamiento:")
print(weights)

# Predicciones finales
print("\nPredicciones finales:")
print(predictions)
