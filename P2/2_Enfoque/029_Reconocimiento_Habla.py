import numpy as np
from os import system

# Simulación simple de estados ocultos para reconocimiento de palabras

# Definimos los estados (fonemas o palabras)
states = ['silencio', 'hola', 'adios']

# Probabilidades de transición entre los estados
transitions = {
    'silencio': {'silencio': 0.6, 'hola': 0.2, 'adios': 0.2},
    'hola':     {'silencio': 0.3, 'hola': 0.4, 'adios': 0.3},
    'adios':    {'silencio': 0.5, 'hola': 0.2, 'adios': 0.3}
}

# Probabilidades de emisión (observaciones, como características acústicas)
emissions = {
    'silencio': {'low_energy': 0.9, 'high_energy': 0.1},
    'hola':     {'low_energy': 0.4, 'high_energy': 0.6},
    'adios':    {'low_energy': 0.3, 'high_energy': 0.7}
}

# Función para hacer una transición de estados basada en probabilidades
def next_state(current_state):
    return np.random.choice(list(transitions[current_state].keys()), p=list(transitions[current_state].values()))

# Función para generar una observación basada en el estado
def generate_observation(state):
    return np.random.choice(list(emissions[state].keys()), p=list(emissions[state].values()))

# Simulación de una secuencia de observaciones (reconocimiento de voz)
def reconocimiento_voz(num_observaciones=10):
    state = 'silencio'  # Inicia en silencio
    observaciones = []
    estados = []
    
    for _ in range(num_observaciones):
        state = next_state(state)
        observacion = generate_observation(state)
        observaciones.append(observacion)
        estados.append(state)
    
    return estados, observaciones

# Simulación del reconocimiento
estados, observaciones = reconocimiento_voz(15)

# Mostrar secuencia de estados y observaciones
system('cls')
print("Estados: ", estados)
print("Observaciones: ", observaciones)