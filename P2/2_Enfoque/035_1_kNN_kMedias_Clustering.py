import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from os import system

#Ejemplo de k-Medias
# Generar datos sintéticos
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Crear el modelo k-Medias
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Predecir los clusters
y_kmeans = kmeans.predict(X)

# Visualizar los resultados
system('cls')
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title("Agrupamiento k-Medias")
plt.show()
