import numpy as np
from os import system

# Estados ocultos: Soleado (0), Lluvioso (1)
states = [0, 1]

# Observaciones: No Paraguas (0), Paraguas (1)
observations = [0, 1]

# Matriz de transición de estados (A)
# P(next_state | current_state)
transition_matrix = np.array([[0.8, 0.2],   # Soleado -> Soleado, Soleado -> Lluvioso
                            [0.4, 0.6]])    # Lluvioso -> Soleado, Lluvioso -> Lluvioso

# Matriz de emisión (B)
# P(observation | state)
emission_matrix = np.array([[0.9, 0.1],  # Soleado -> No Paraguas, Paraguas
                            [0.3, 0.7]]) # Lluvioso -> No Paraguas, Paraguas

# Probabilidades iniciales de los estados (π)
initial_state_probs = np.array([0.6, 0.4])  # P(Soleado) = 0.6, P(Lluvioso) = 0.4

def forward_algorithm(observations_seq, transition_matrix, emission_matrix, initial_state_probs):
    num_states = len(transition_matrix)
    num_observations = len(observations_seq)

    # Matriz alpha donde alpha[t][i] es la probabilidad de la observación hasta el tiempo t y el estado i
    alpha = np.zeros((num_observations, num_states))

    # Inicialización
    alpha[0, :] = initial_state_probs * emission_matrix[:, observations_seq[0]]

    # Iteración hacia adelante
    for t in range(1, num_observations):
        for j in range(num_states):
            alpha[t, j] = emission_matrix[j, observations_seq[t]] * np.sum(alpha[t-1, :] * transition_matrix[:, j])

    # Probabilidad total de la secuencia de observaciones
    return np.sum(alpha[-1, :])

# Secuencia de observaciones (0 = No Paraguas, 1 = Paraguas)
observations_seq = [0, 1, 1, 0, 1]

# Ejecutar el algoritmo hacia adelante
system('cls')
prob_observations = forward_algorithm(observations_seq, transition_matrix, emission_matrix, initial_state_probs)
print(f"Probabilidad de la secuencia observada: {prob_observations:.4f}")

def viterbi_algorithm(observations_seq, transition_matrix, emission_matrix, initial_state_probs):
    num_states = len(transition_matrix)
    num_observations = len(observations_seq)

    # Matriz delta: guarda las probabilidades máximas hasta el tiempo t
    delta = np.zeros((num_observations, num_states))

    # Matriz psi: guarda los estados más probables
    psi = np.zeros((num_observations, num_states), dtype=int)

    # Inicialización
    delta[0, :] = initial_state_probs * emission_matrix[:, observations_seq[0]]

    # Iteración hacia adelante
    for t in range(1, num_observations):
        for j in range(num_states):
            max_prob = np.max(delta[t-1, :] * transition_matrix[:, j])
            delta[t, j] = emission_matrix[j, observations_seq[t]] * max_prob
            psi[t, j] = np.argmax(delta[t-1, :] * transition_matrix[:, j])

    # Encontrar la secuencia más probable de estados
    states_seq = np.zeros(num_observations, dtype=int)
    states_seq[-1] = np.argmax(delta[-1, :])

    for t in range(num_observations-2, -1, -1):
        states_seq[t] = psi[t+1, states_seq[t+1]]

    return states_seq

# Ejecutar el algoritmo de Viterbi
states_seq = viterbi_algorithm(observations_seq, transition_matrix, emission_matrix, initial_state_probs)
print(f"Secuencia de estados más probable: {states_seq}")
