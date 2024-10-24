import numpy as np
from os import system

class HammingNetwork:
    def __init__(self, n_inputs, n_outputs):
        self.weights = np.zeros((n_outputs, n_inputs))

    def train(self, X, y):
        for i in range(len(X)):
            self.weights[y[i]] += X[i]

    def predict(self, X):
        return np.argmax(np.dot(self.weights, X.T), axis=0)

# Ejemplo de uso
system('cls')
X = np.array([[1, 0, 1], [0, 1, 1]])  # Entradas
y = np.array([0, 1])  # Salidas
hamming_net = HammingNetwork(n_inputs=3, n_outputs=2)
hamming_net.train(X, y)
predictions = hamming_net.predict(X)
print(predictions)

class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        for p in patterns:
            self.weights += np.outer(p, p)
        np.fill_diagonal(self.weights, 0)

    def predict(self, input_pattern, steps=5):
        for _ in range(steps):
            for i in range(len(input_pattern)):
                net_input = np.dot(self.weights[i], input_pattern)
                input_pattern[i] = 1 if net_input > 0 else -1
        return input_pattern

# Ejemplo de uso
hopfield_net = HopfieldNetwork(n_neurons=4)
patterns = np.array([[1, -1, -1, 1], [-1, 1, 1, -1]])
hopfield_net.train(patterns)
output = hopfield_net.predict(np.array([1, -1, -1, -1]))
print(output)

class HebbianNetwork:
    def __init__(self, n_neurons):
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, X):
        for x in X:
            self.weights += np.outer(x, x)

# Ejemplo de uso
hebbian_net = HebbianNetwork(n_neurons=3)
X = np.array([[1, 0, -1], [0, 1, 1]])
hebbian_net.train(X)
print(hebbian_net.weights)

class BoltzmannMachine:
    def __init__(self, n_visible, n_hidden):
        self.n_visible = n_visible
        self.n_hidden = n_hidden
        self.weights = np.random.randn(n_visible, n_hidden) * 0.1

    def train(self, data, epochs):
        # Implementar el algoritmo de entrenamiento aquí
        pass

# Ejemplo de uso
bm = BoltzmannMachine(n_visible=3, n_hidden=2)