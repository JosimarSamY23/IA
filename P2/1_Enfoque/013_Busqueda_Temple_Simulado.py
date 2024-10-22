import math
import random
from os import system

# Implementación del algoritmo de temple simulado
class TempleSimulado:
    def __init__(self, grafo, heuristica, temperatura_inicial, tasa_enfriamiento):
        self.grafo = grafo
        self.heuristica = heuristica
        self.temperatura_inicial = temperatura_inicial
        self.tasa_enfriamiento = tasa_enfriamiento

    def temple_simulado(self, inicio, objetivo):
        nodo_actual = inicio
        mejor_nodo = nodo_actual
        mejor_heuristica = self.heuristica[nodo_actual]
        temperatura = self.temperatura_inicial
        camino = [nodo_actual]

        while temperatura > 0.1:  # Criterio de parada basado en temperatura
            vecinos = self.grafo[nodo_actual]
            
            # Si no hay más vecinos, detener la búsqueda
            if not vecinos:
                break

            # Seleccionamos un vecino aleatorio
            vecino, _ = random.choice(vecinos)
            delta_heuristica = self.heuristica[vecino] - self.heuristica[nodo_actual]

            # Si el vecino es mejor o se acepta con probabilidad, movemos
            if delta_heuristica < 0 or random.uniform(0, 1) < math.exp(-delta_heuristica / temperatura):
                nodo_actual = vecino
                camino.append(nodo_actual)
                
                # Actualizar la mejor solución encontrada
                if self.heuristica[nodo_actual] < mejor_heuristica:
                    mejor_nodo = nodo_actual
                    mejor_heuristica = self.heuristica[nodo_actual]

            # Enfriamiento
            temperatura *= self.tasa_enfriamiento

            # Si llegamos al objetivo, detener
            if nodo_actual == objetivo:
                print("Objetivo alcanzado.")
                return camino

        print("Búsqueda detenida debido a baja temperatura o no se encontró el objetivo.")
        return camino

# Grafo representado como un diccionario (lista de adyacencia con costos)
system('cls')
grafo = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heurística (estimación cuán lejos está cada nodo del objetivo 'F')
heuristica = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

# Crear el objeto de temple simulado
temple = TempleSimulado(grafo, heuristica, temperatura_inicial=100, tasa_enfriamiento=0.95)

# Ingresar el nodo de inicio
try:
    while True:
        nodo_inicio = input("Selecciona el nodo en donde comenzar  (A-F): ").upper()
        nodo_final  = input("Selecciona el nodo en donde finalizar (A-F): ").upper()

        if nodo_inicio in grafo.keys() and nodo_final in grafo.keys():
            break
        else:
            print("Valor de un nodo no está dentro del rango de valores")

except Exception:
    print("Ingresa una opción correcta")

# Ejemplo de búsqueda de temple simulado desde el nodo 'x' hasta el nodo 'y'
camino_temple = temple.temple_simulado(nodo_inicio, nodo_final)
print(f"Camino encontrado con temple simulado: {camino_temple}")
