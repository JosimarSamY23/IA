import numpy as np
from os import system

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Ejemplo de uso
system('cls')
x = np.array([-2, -1, 0, 1, 2])
output = sigmoid(x)
print("Sigmoide             :", output)

def tanh(x):
    return np.tanh(x)

# Ejemplo de uso
output = tanh(x)
print("Tangente hiperbólica :", output)

def relu(x):
    return np.maximum(0, x)

# Ejemplo de uso
output = relu(x)
print("ReLU                 :", output)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Ejemplo de uso
output = leaky_relu(x)
print("Leaky ReLU           :", output)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Para estabilidad numérica
    return exp_x / exp_x.sum(axis=0)

# Ejemplo de uso
x = np.array([2.0, 1.0, 0.1])
output = softmax(x)
print("Softmax              :", output)
