import numpy as np
import matplotlib.pyplot as plt
from os import system

# Función para calcular la probabilidad posterior usando el teorema de Bayes
def posterior(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

# Definimos una función de verosimilitud (la probabilidad de los datos dados diferentes sesgos de la moneda)
def likelihood(theta, datos):
    heads = np.sum(datos == 1)  # Número de caras
    tails = np.sum(datos == 0)  # Número de cruces
    return (theta ** heads) * ((1 - theta) ** tails)

# Datos observados: 1 = cara, 0 = cruz
datos = np.array([1, 0, 1, 1, 0, 1, 1, 0, 1, 1])

# Prior: Distribución uniforme sobre el sesgo (hipótesis de que la moneda es justa o sesgada)
theta_values = np.linspace(0, 1, 100)  # Valores posibles del sesgo (0 a 1)
prior = np.ones(len(theta_values))  # Prior uniforme (creemos que todos los sesgos son igualmente probables)

# Calculamos la verosimilitud para cada valor de sesgo posible
likelihoods = np.array([likelihood(theta, datos) for theta in theta_values])

# La evidencia es el total de la verosimilitud multiplicada por el prior
evidence = np.sum(likelihoods * prior)

# Aplicamos el teorema de Bayes para obtener la probabilidad posterior
posterior_prob = posterior(prior, likelihoods, evidence)

# Normalización del posterior
posterior_prob /= np.sum(posterior_prob)

# Graficar la distribución posterior
system('cls')
plt.plot(theta_values, posterior_prob, label='Posterior')
plt.xlabel('Sesgo de la moneda (θ)')
plt.ylabel('Probabilidad Posterior')
plt.title('Aprendizaje Bayesiano: Posterior del sesgo de la moneda')
plt.legend()
plt.show()
