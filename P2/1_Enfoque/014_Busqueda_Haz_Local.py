import random
from os import system

# Implementación del algoritmo de búsqueda de haz local
class BusquedaHazLocal:
    def __init__(self, grafo, heuristica, tam_haz=3, max_iteraciones=20):
        self.grafo = grafo
        self.heuristica = heuristica
        self.tam_haz = tam_haz
        self.max_iteraciones = max_iteraciones

    def busqueda_haz_local(self, inicio, objetivo):
        # Inicializar el haz con soluciones aleatorias
        haz_actual = [inicio] * self.tam_haz
        caminos = [[inicio] for _ in range(self.tam_haz)]

        for iteracion in range(self.max_iteraciones):
            vecinos = []
            nuevos_caminos = []

            # Para cada solución en el haz actual, generar todos los vecinos
            for i, nodo in enumerate(haz_actual):
                if nodo in self.grafo:
                    for vecino, _ in self.grafo[nodo]:
                        vecinos.append((vecino, caminos[i] + [vecino]))
            
            # Ordenar los vecinos según la heurística
            vecinos = sorted(vecinos, key=lambda x: self.heuristica[x[0]])

            # Mantener solo los mejores 'tam_haz' vecinos
            haz_actual = [vecino for vecino, _ in vecinos[:self.tam_haz]]
            caminos = [camino for _, camino in vecinos[:self.tam_haz]]

            # Si alguno de los caminos llega al objetivo, detener
            for camino in caminos:
                if camino[-1] == objetivo:
                    print(f"Objetivo alcanzado en la iteración {iteracion + 1}")
                    return camino

        print(f"Objetivo no encontrado después de {self.max_iteraciones} iteraciones.")
        return caminos

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

# Crear el objeto de búsqueda de haz local
busqueda = BusquedaHazLocal(grafo, heuristica, tam_haz=2, max_iteraciones=10)

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

# Ejemplo de búsqueda de haz local desde el nodo 'x' hasta el nodo 'y'
camino_haz_local = busqueda.busqueda_haz_local(nodo_inicio, nodo_final)
print(f"Camino encontrado con búsqueda de haz local: {camino_haz_local}")
