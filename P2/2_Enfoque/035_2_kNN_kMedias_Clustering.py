import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from os import system

#Ejemplo de Clustering con DBSCAN
# Generar datos sintéticos
X, _ = make_moons(n_samples=300, noise=0.05)

# Aplicar DBSCAN
dbscan = DBSCAN(eps=0.2, min_samples=5)
clusters = dbscan.fit_predict(X)

# Visualizar los resultados
system('cls')
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.title("Clustering con DBSCAN")
plt.show()
