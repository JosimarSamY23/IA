import numpy as np
from os import system

# Definir los estados ocultos (palabras que queremos reconocer)
estados = ['Hola', 'Mundo', 'Adiós']
num_estados = len(estados)

# Definir las probabilidades iniciales de los estados
prob_iniciales = np.array([0.5, 0.3, 0.2])  # Ejemplo: más probable comenzar con "Hola"

# Definir la matriz de transición de estados (transiciones entre palabras)
transiciones = np.array([
    [0.6, 0.3, 0.1],  # Probabilidades de transición desde "Hola"
    [0.2, 0.6, 0.2],  # Probabilidades de transición desde "Mundo"
    [0.1, 0.3, 0.6],  # Probabilidades de transición desde "Adiós"
])

# Definir la matriz de emisión (cómo los estados generan observaciones)
# Las observaciones son índices de características acústicas hipotéticas (0, 1, 2)
emisiones = np.array([
    [0.7, 0.2, 0.1],  # Observaciones desde "Hola"
    [0.1, 0.7, 0.2],  # Observaciones desde "Mundo"
    [0.1, 0.2, 0.7],  # Observaciones desde "Adiós"
])

# Generar una secuencia de observaciones ruidosas
def generar_observaciones(num_observaciones):
    observaciones = []
    estado_actual = np.random.choice(estados, p=prob_iniciales)
    for _ in range(num_observaciones):
        estado_indice = estados.index(estado_actual)
        observacion = np.random.choice([0, 1, 2], p=emisiones[estado_indice])
        observaciones.append(observacion)
        # Transición al siguiente estado
        estado_actual = np.random.choice(estados, p=transiciones[estado_indice])
    return observaciones

# Algoritmo de Viterbi para encontrar la secuencia más probable de palabras
def viterbi(observaciones):
    num_observaciones = len(observaciones)
    V = np.zeros((num_estados, num_observaciones))
    camino = np.zeros((num_estados, num_observaciones), dtype=int)
    
    # Inicialización
    for i in range(num_estados):
        V[i, 0] = prob_iniciales[i] * emisiones[i, observaciones[0]]
    
    # Iteración
    for t in range(1, num_observaciones):
        for j in range(num_estados):
            max_prob = V[0, t-1] * transiciones[0, j]
            max_state = 0
            for i in range(1, num_estados):
                prob = V[i, t-1] * transiciones[i, j]
                if prob > max_prob:
                    max_prob = prob
                    max_state = i
            V[j, t] = max_prob * emisiones[j, observaciones[t]]
            camino[j, t] = max_state
    
    # Backtracking para obtener la secuencia óptima
    mejor_camino = np.zeros(num_observaciones, dtype=int)
    mejor_camino[-1] = np.argmax(V[:, -1])
    
    for t in range(num_observaciones-2, -1, -1):
        mejor_camino[t] = camino[mejor_camino[t+1], t+1]
    
    return [estados[i] for i in mejor_camino]

# Simular una secuencia de observaciones
system('cls')
num_observaciones = 10
observaciones = generar_observaciones(num_observaciones)
print(f"Observaciones: {observaciones}")

# Reconocer la secuencia de palabras usando Viterbi
palabras_reconocidas = viterbi(observaciones)
print(f"Secuencia reconocida de palabras: {palabras_reconocidas}")
