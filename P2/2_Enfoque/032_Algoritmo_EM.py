import numpy as np
import matplotlib.pyplot as plt
from os import system

# Generar datos sintéticos de dos distribuciones gaussianas
np.random.seed(42)
n_samples = 300
X = np.concatenate([
    np.random.normal(loc=-2, scale=0.5, size=n_samples // 2),
    np.random.normal(loc=3, scale=0.5, size=n_samples // 2)
]).reshape(-1, 1)

# Visualizar los datos generados
plt.hist(X, bins=30, density=True)
plt.title('Datos Sintéticos')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()

# Implementación del Algoritmo EM para GMM
def em_algorithm(X, n_components, n_iterations=100):
    n_samples, n_features = X.shape
    
    # Inicialización
    np.random.seed(42)
    weights = np.ones(n_components) / n_components
    means = np.random.choice(X.flatten(), size=n_components)
    variances = np.ones(n_components)

    for iteration in range(n_iterations):
        # Paso E: Cálculo de la responsabilidad
        responsibilities = np.zeros((n_samples, n_components))

        for k in range(n_components):
            # Ajustar dimensiones
            diff = X.flatten() - means[k]  # Aplanar X para la resta
            responsibilities[:, k] = weights[k] * (1 / np.sqrt(2 * np.pi * variances[k])) * np.exp(-0.5 * (diff ** 2) / variances[k])
        
        responsibilities /= responsibilities.sum(axis=1, keepdims=True)

        # Paso M: Actualización de parámetros
        for k in range(n_components):
            N_k = responsibilities[:, k].sum()
            weights[k] = N_k / n_samples
            means[k] = (responsibilities[:, k] @ X.flatten()) / N_k
            variances[k] = ((responsibilities[:, k] * (X.flatten() - means[k]) ** 2).sum()) / N_k

    return weights, means, variances

# Ejecutar el algoritmo EM
n_components = 2
weights, means, variances = em_algorithm(X, n_components)

# Mostrar resultados
system('cls')
print("Pesos:    ", weights)
print("Medias:   ", means)
print("Varianzas:", variances)

# Visualizar los resultados
plt.hist(X, bins=30, density=True, alpha=0.5, label='Datos')
x = np.linspace(-5, 5, 1000).reshape(-1, 1)
for k in range(n_components):
    plt.plot(x, weights[k] * (1 / np.sqrt(2 * np.pi * variances[k])) * np.exp(-0.5 * ((x.flatten() - means[k]) ** 2) / variances[k]), label=f'Componente {k+1}')
plt.title('Modelo de Mezcla Gaussiana (GMM)')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.legend()
plt.show()
