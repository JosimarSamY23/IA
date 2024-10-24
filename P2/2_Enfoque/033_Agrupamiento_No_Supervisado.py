import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from os import system

# Generar datos sintéticos
np.random.seed(42)
n_samples = 500
X = np.concatenate([
    np.random.normal(loc=-2, scale=0.5, size=n_samples // 2),
    np.random.normal(loc=3, scale=0.5, size=n_samples // 2)
]).reshape(-1, 1)

# Visualizar los datos generados
plt.scatter(X, np.zeros_like(X), alpha=0.5)
plt.title('Datos Sintéticos')
plt.xlabel('Valor')
plt.show()

# Aplicar K-Means
k = 2  # Número de clústeres
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizar los resultados
system('cls')
plt.scatter(X, np.zeros_like(X), c=labels, cmap='viridis', alpha=0.5)
plt.scatter(centroids, np.zeros_like(centroids), c='red', marker='X', s=200, label='Centroides')
plt.title('Resultados del Agrupamiento K-Means')
plt.xlabel('Valor')
plt.legend()
plt.show()
