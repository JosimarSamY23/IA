import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from os import system

# Generar un conjunto de datos de ejemplo
X, y = make_moons(n_samples=1000, noise=0.2, random_state=0)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar la red neuronal multicapa
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=1)
mlp.fit(X_train, y_train)

# Evaluar el rendimiento del modelo
accuracy = mlp.score(X_test, y_test)
print(f'Precisión del modelo: {accuracy:.2f}')

# Graficar la decisión de la red neuronal
def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.5, cmap='coolwarm')
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap='coolwarm')
    plt.title('Frente de Decisión de la MLP')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

# Graficar la frontera de decisión
system('cls')
plot_decision_boundary(mlp, X_test, y_test)
