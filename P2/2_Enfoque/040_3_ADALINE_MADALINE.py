import numpy as np
from os import system

class MADALINE:
    def __init__(self, n_neurons=2, learning_rate=0.01, n_iter=1000):
        self.n_neurons = n_neurons
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros((self.n_neurons, n_features))
        self.bias = np.zeros(self.n_neurons)

        for _ in range(self.n_iter):
            for idx, x_i in enumerate(X):
                for neuron in range(self.n_neurons):
                    linear_output = np.dot(x_i, self.weights[neuron]) + self.bias[neuron]
                    error = y[idx] - linear_output
                    self.weights[neuron] += self.learning_rate * error * x_i
                    self.bias[neuron] += self.learning_rate * error

    def predict(self, X):
        linear_output = np.dot(X, self.weights.T) + self.bias
        return np.where(linear_output >= 0, 1, 0)

# Ejemplo de uso
system('cls')
if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  # Salida de AND

    madaline = MADALINE(n_neurons=2, learning_rate=0.01, n_iter=10)
    madaline.fit(X, y)
    print("Pesos        :", madaline.weights)
    print("Bias         :", madaline.bias)
    print("Predicciones :", madaline.predict(X))
