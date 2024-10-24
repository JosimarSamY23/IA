import numpy as np
from os import system

class ADALINE:
    def __init__(self, learning_rate=0.01, n_iter=1000):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iter):
            linear_output = np.dot(X, self.weights) + self.bias
            errors = y - linear_output

            # Update weights and bias
            self.weights += self.learning_rate * X.T.dot(errors)
            self.bias += self.learning_rate * errors.sum()

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return linear_output

# Ejemplo de uso
system('cls')
if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  # Salida de AND

    adaline = ADALINE(learning_rate=0.01, n_iter=10)
    adaline.fit(X, y)
    print("Pesos        :", adaline.weights)
    print("Bias         :", adaline.bias)
    print("Predicciones :", adaline.predict(X))
