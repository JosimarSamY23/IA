import numpy as np
from os import system

# Definir la función de activación (función sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide (para retropropagación)
def sigmoid_derivative(x):
    return x * (1 - x)

# Entradas y salidas de entrenamiento
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
y = np.array([[0], [1], [1], [0]])              # Salida esperada (XOR)

# Inicializar pesos aleatorios
np.random.seed(1)
weights = np.random.rand(2, 1)
bias = np.random.rand(1)

# Tasa de aprendizaje
learning_rate = 0.1
epochs = 10000  # Número de iteraciones

# Entrenamiento de la neurona
for epoch in range(epochs):
    # Paso hacia adelante
    z = np.dot(X, weights) + bias
    output = sigmoid(z)

    # Calcular el error
    error = y - output

    # Retropropagación del error
    adjustments = error * sigmoid_derivative(output)
    weights += np.dot(X.T, adjustments) * learning_rate
    bias += np.sum(adjustments) * learning_rate

# Mostrar pesos finales y bias
system('cls')
print("Pesos finales: ", weights)
print("\nBias final   : ", bias)

# Probar la neurona
z_test = np.dot(X, weights) + bias
output_test = sigmoid(z_test)
print("\nPredicciones: ", output_test)
