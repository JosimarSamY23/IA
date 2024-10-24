import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from os import system

# Crear un conjunto de datos linealmente separable
X_separable, y_separable = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=1.0)

# Crear un conjunto de datos no linealmente separable
X_non_separable = np.array([[1, 1], [2, 2], [3, 1], [4, 2], [5, 5], [1, 5], [5, 1]])
y_non_separable = np.array([0, 0, 0, 1, 1, 1, 1])

# Graficar los datos linealmente separables
system('cls')
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_separable[:, 0], X_separable[:, 1], c=y_separable, cmap='coolwarm', edgecolors='k')
plt.title('Datos Linealmente Separables')
plt.xlabel('X1')
plt.ylabel('X2')

# Graficar los datos no linealmente separables
plt.subplot(1, 2, 2)
plt.scatter(X_non_separable[:, 0], X_non_separable[:, 1], c=y_non_separable, cmap='coolwarm', edgecolors='k')
plt.title('Datos No Linealmente Separables')
plt.xlabel('X1')
plt.ylabel('X2')

plt.tight_layout()
plt.show()