import numpy as np
from os import system

# Definir las variables
variables = ['Incendio', 'Detector de Humo', 'Alarma']

# Definir las probabilidades de cada variable
prob_incendio = 0.01  # Probabilidad de que haya un incendio
prob_detector_dado_incendio = 0.9  # Probabilidad de que el detector detecte humo dado que hay un incendio
prob_detector_dado_no_incendio = 0.2  # Probabilidad de que el detector detecte humo sin incendio (falso positivo)
prob_alarma_dado_detector = 0.95  # Probabilidad de que suene la alarma si se detecta humo
prob_alarma_dado_no_detector = 0.05  # Probabilidad de que suene la alarma sin detección de humo

# Función para simular el evento "Incendio"
def simular_incendio():
    return np.random.rand() < prob_incendio

# Función para simular el evento "Detector de Humo"
def simular_detector(incendio):
    if incendio:
        return np.random.rand() < prob_detector_dado_incendio
    else:
        return np.random.rand() < prob_detector_dado_no_incendio

# Función para simular el evento "Alarma"
def simular_alarma(detector):
    if detector:
        return np.random.rand() < prob_alarma_dado_detector
    else:
        return np.random.rand() < prob_alarma_dado_no_detector

# Simular eventos en la red bayesiana
def simular_red_bayesiana():
    incendio = simular_incendio()
    detector = simular_detector(incendio)
    alarma = simular_alarma(detector)

    return {'Incendio': incendio, 'Detector de Humo': detector, 'Alarma': alarma}

# Simular 10 veces la red bayesiana
system('cls')
for i in range(10):
    resultado = simular_red_bayesiana()
    print(f"Simulación {i+1}: {resultado}")
