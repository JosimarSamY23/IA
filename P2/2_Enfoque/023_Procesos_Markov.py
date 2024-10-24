import numpy as np
import matplotlib.pyplot as plt
from os import system

# Definimos la matriz de transición para un proceso de Markov con 3 estados
# Las filas representan el estado actual, y las columnas el siguiente estado
transition_matrix = np.array([[0.5, 0.3, 0.2],  # Desde el estado 0
                            [0.2, 0.6, 0.2],    # Desde el estado 1
                            [0.1, 0.3, 0.6]])   # Desde el estado 2

# Definimos los estados
states = [0, 1, 2]

# Función para simular el proceso de Markov
def simulate_markov_chain(transition_matrix, initial_state, num_steps):
    current_state = initial_state
    trajectory = [current_state]
    
    for _ in range(num_steps):
        current_state = np.random.choice(states, p=transition_matrix[current_state])
        trajectory.append(current_state)
    
    return trajectory

# Simulación de 50 pasos comenzando en el estado 0
num_steps = 50
initial_state = 0
trajectory = simulate_markov_chain(transition_matrix, initial_state, num_steps)

# Gráfico del estado a través del tiempo
system('cls')
plt.plot(trajectory, marker='o')
plt.title('Simulación de un Proceso de Markov')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.grid(True)
plt.show()

# Verificar si la transición depende solo del estado actual
for t in range(1, num_steps):
    current_state = trajectory[t]
    previous_state = trajectory[t-1]
    print(f"Paso {t}: Estado anterior = {previous_state}, Estado actual = {current_state}")
