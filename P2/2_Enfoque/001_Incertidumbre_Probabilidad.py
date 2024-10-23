import numpy as np
from os import system

# Estados (posiciones en la cuadrícula)
states = np.array([0, 1, 2, 3, 4])  # El robot puede estar en una de estas 5 posiciones

# Definir las probabilidades de transición
# Queremos movernos a la derecha (acción principal), pero con un 20% de error
transition_matrix = {
    0: [0.8, 0.2, 0, 0, 0],    # Probabilidad de moverse a la derecha desde el estado 0
    1: [0.1, 0.8, 0.1, 0, 0],  # Probabilidad de moverse a la derecha desde el estado 1
    2: [0, 0.1, 0.8, 0.1, 0],  # Probabilidad de moverse a la derecha desde el estado 2
    3: [0, 0, 0.1, 0.8, 0.1],  # Probabilidad de moverse a la derecha desde el estado 3
    4: [0, 0, 0, 0.2, 0.8],    # Probabilidad de moverse a la derecha desde el estado 4
}

# Definir el estado inicial
initial_state = 2  # El robot empieza en la posición 2

# Simulación de los movimientos del robot
num_steps = 10          # Número de pasos a simular
state = initial_state   # Estado inicial
trajectory = [state]    # Registro de la trayectoria

for step in range(num_steps):
    # Obtener las probabilidades de transición para el estado actual
    probabilities = transition_matrix[state]
    
    # Elegir el siguiente estado basado en las probabilidades
    next_state = np.random.choice(states, p=probabilities)
    
    # Actualizar el estado actual
    state = next_state
    trajectory.append(state)

# Mostrar la trayectoria del robot
system('cls')
print(f"Trayectoria del robot: {trajectory}")
