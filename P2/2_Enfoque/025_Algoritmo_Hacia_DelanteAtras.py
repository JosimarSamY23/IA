import numpy as np
from os import system

# Estados ocultos: Soleado (0), Lluvioso (1)
states = [0, 1]

# Probabilidad de transición entre estados (matriz de transición)
# P(next_state | current_state)
transition_matrix = np.array([[0.7, 0.3],   # Soleado -> Soleado, Soleado -> Lluvioso
                            [0.4, 0.6]])    # Lluvioso -> Soleado, Lluvioso -> Lluvioso

# Probabilidad de observación (emisión): Soleado (0) o Lluvioso (1) observados
# P(observation | state)
observation_matrix = np.array([[0.9, 0.1],  # Soleado -> Observamos "Soleado", "Lluvioso"
                            [0.2, 0.8]])    # Lluvioso -> Observamos "Soleado", "Lluvioso"

# Probabilidades iniciales del estado
initial_state_probs = np.array([0.6, 0.4])  # P(Soleado) = 0.6, P(Lluvioso) = 0.4

# Observaciones (ruidosas)
# 0 = Observamos "Soleado", 1 = Observamos "Lluvioso"
observations = [0, 0, 1, 0, 1, 1, 0, 1]

def forward(observations, transition_matrix, observation_matrix, initial_state_probs):
    num_states = transition_matrix.shape[0]
    num_observations = len(observations)

    # Matriz alpha donde alpha[t][i] es la probabilidad de la observación hasta el tiempo t y el estado i
    alpha = np.zeros((num_observations, num_states))

    # Inicialización en t = 0
    alpha[0, :] = initial_state_probs * observation_matrix[:, observations[0]]

    # Iteración hacia adelante
    for t in range(1, num_observations):
        for j in range(num_states):
            alpha[t, j] = observation_matrix[j, observations[t]] * np.sum(alpha[t-1, :] * transition_matrix[:, j])

    return alpha

def backward(observations, transition_matrix, observation_matrix):
    num_states = transition_matrix.shape[0]
    num_observations = len(observations)

    # Matriz beta donde beta[t][i] es la probabilidad de las observaciones futuras dado el estado i en el tiempo t
    beta = np.zeros((num_observations, num_states))

    # Inicialización en t = T (último tiempo)
    beta[-1, :] = 1

    # Iteración hacia atrás
    for t in range(num_observations - 2, -1, -1):
        for i in range(num_states):
            beta[t, i] = np.sum(transition_matrix[i, :] * observation_matrix[:, observations[t+1]] * beta[t+1, :])

    return beta

def forward_backward(observations, transition_matrix, observation_matrix, initial_state_probs):
    # Paso hacia adelante
    alpha = forward(observations, transition_matrix, observation_matrix, initial_state_probs)
    
    # Paso hacia atrás
    beta = backward(observations, transition_matrix, observation_matrix)
    
    # Calcular la probabilidad posterior
    posterior_probs = (alpha * beta) / np.sum(alpha * beta, axis=1, keepdims=True)
    
    return posterior_probs

# Ejecutar el algoritmo hacia adelante y hacia atrás
posterior_probs = forward_backward(observations, transition_matrix, observation_matrix, initial_state_probs)

# Imprimir las probabilidades suavizadas
system('cls')
for t, probs in enumerate(posterior_probs):
    print(f"Tiempo {t}: P(Soleado) = {probs[0]:.4f}, P(Lluvioso) = {probs[1]:.4f}")
