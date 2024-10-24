import numpy as np
from os import system

# Número de partículas
num_particulas = 400

# Modelo de transición de estados
def transicion_estado(x):
    return x + np.random.normal(0, 1)  # Agrega ruido gaussiano

# Modelo de observación (likelihood)
def observacion_prob(x, z):
    return np.exp(-0.5 * ((z - x) ** 2) / 1)  # Asume que la observación está cerca del estado

# Inicialización
particulas = np.random.uniform(-10, 10, num_particulas)  # Partículas iniciales
pesos = np.ones(num_particulas) / num_particulas  # Pesos iniciales

# Filtrado de Partículas
def filtro_particulas(observaciones):
    global particulas, pesos
    for z in observaciones:
        # 1. Predicción del estado
        particulas = np.array([transicion_estado(p) for p in particulas])

        # 2. Ponderación según las observaciones
        pesos = np.array([observacion_prob(p, z) for p in particulas])

        # 3. Normalización de los pesos
        pesos += 1e-300  # Para evitar divisiones por cero
        pesos /= sum(pesos)

        # 4. Re-muestreo: Selecciona partículas con reemplazo según sus pesos
        indices = np.random.choice(range(num_particulas), num_particulas, p=pesos)
        particulas = particulas[indices]
        pesos = np.ones(num_particulas) / num_particulas  # Reiniciar los pesos

    # Estimación del estado
    return np.mean(particulas)

# Simulación de observaciones
observaciones = [5.0 + np.random.normal(0, 1) for _ in range(10)]  # Observaciones ruidosas

# Ejecutar el filtro de partículas
estado_estimado = filtro_particulas(observaciones)
system('cls')
print("Estado estimado:", estado_estimado)
