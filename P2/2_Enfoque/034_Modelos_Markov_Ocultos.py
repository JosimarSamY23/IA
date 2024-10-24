import numpy as np
from os import system

class SimpleHMM:
    def __init__(self, start_prob, trans_prob, emit_prob):
        self.start_prob = start_prob    # Probabilidades iniciales
        self.trans_prob = trans_prob    # Probabilidades de transición
        self.emit_prob = emit_prob      # Probabilidades de emisión

    def sample(self, n_samples):
        n_states = len(self.start_prob)
        states = np.zeros(n_samples, dtype=int)
        observations = np.zeros(n_samples, dtype=int)

        # Inicializar el estado
        states[0] = np.random.choice(n_states, p=self.start_prob)
        observations[0] = np.random.choice(len(self.emit_prob[0]), p=self.emit_prob[states[0]])

        for t in range(1, n_samples):
            # Transición al siguiente estado
            states[t] = np.random.choice(n_states, p=self.trans_prob[states[t-1]])
            # Generar la observación correspondiente
            observations[t] = np.random.choice(len(self.emit_prob[0]), p=self.emit_prob[states[t]])

        return states, observations

# Definir los parámetros del HMM
start_prob = np.array([0.6, 0.3, 0.1])                                                 # Probabilidad inicial de los estados
trans_prob = np.array([[0.7, 0.2, 0.1],[0.1, 0.6, 0.3],[0.2, 0.3, 0.5]])               # Probabilidades de transición
emit_prob = np.array([[0.5, 0.5, 0.0, 0.0],[0.0, 0.5, 0.5, 0.0],[0.0, 0.0, 0.5, 0.5]]) # Probabilidades de emisión

# Crear el modelo HMM
hmm = SimpleHMM(start_prob, trans_prob, emit_prob)

# Generar una secuencia de observaciones
n_samples = 100
states, observations = hmm.sample(n_samples)

# Mostrar resultados
system('cls')
print("Estados ocultos: ", states)
print("\nObservaciones  : ", observations)
