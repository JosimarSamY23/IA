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

def filtering(observations, transition_matrix, observation_matrix, initial_state_probs):
    num_states = transition_matrix.shape[0]
    belief = initial_state_probs
    beliefs = [belief]

    for obs in observations:
        # Predicción: aplicar matriz de transición
        belief_pred = np.dot(belief, transition_matrix)

        # Actualización: aplicar matriz de observación
        belief_upd = belief_pred * observation_matrix[:, obs]

        # Normalización para asegurarnos de que es una distribución de probabilidad
        belief = belief_upd / np.sum(belief_upd)
        beliefs.append(belief)

    return beliefs

# Filtramos la serie de observaciones
beliefs = filtering(observations, transition_matrix, observation_matrix, initial_state_probs)

# Imprimimos las creencias para cada observación
system('cls')
for t, belief in enumerate(beliefs):
    print(f"Tiempo {t}: P(Soleado) = {belief[0]:.4f}, P(Lluvioso) = {belief[1]:.4f}")

def prediction(belief, transition_matrix, num_steps):
    for _ in range(num_steps):
        belief = np.dot(belief, transition_matrix)
    return belief

# Predecir estado futuro después de 3 pasos
future_belief = prediction(beliefs[-1], transition_matrix, 3)
print(f"\nPredicción: P(Soleado) = {future_belief[0]:.4f}, P(Lluvioso) = {future_belief[1]:.4f}")

def smoothing(observations, beliefs, transition_matrix):
    num_steps = len(observations)
    smoothed_beliefs = [beliefs[-1]]  # Comienza con el último estado creído

    # Iteración hacia atrás (backward pass)
    for t in range(num_steps - 1, 0, -1):
        belief_next = smoothed_beliefs[0]
        belief = beliefs[t-1]
        smoothing_factor = np.dot(transition_matrix, belief_next) / np.dot(belief, transition_matrix)
        smoothed_belief = belief * smoothing_factor
        smoothed_beliefs.insert(0, smoothed_belief)

    return smoothed_beliefs

# Realizar suavizado
smoothed_beliefs = smoothing(observations, beliefs, transition_matrix)

# Imprimimos las creencias suavizadas para cada observación
print("")
for t, belief in enumerate(smoothed_beliefs):
    print(f"Suavizado Tiempo {t}: P(Soleado) = {belief[0]:.4f}, P(Lluvioso) = {belief[1]:.4f}")
