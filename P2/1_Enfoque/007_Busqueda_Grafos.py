from collections import deque
from os import system

# Clase para implementar diferentes tipos de búsqueda en grafos
class BusquedaGrafo:
    def __init__(self, grafo):
        self.grafo = grafo

    # Búsqueda en Anchura (BFS)
    def busqueda_anchura(self, inicio, objetivo):
        cola = deque([inicio])
        visitados = {inicio: None}

        while cola:
            nodo_actual = cola.popleft()

            # Si encontramos el objetivo
            if nodo_actual == objetivo:
                return self._reconstruir_camino(visitados, inicio, objetivo)

            # Explorar vecinos no visitados
            for vecino in self.grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados[vecino] = nodo_actual
                    cola.append(vecino)

        return None  # Si no se encuentra el objetivo

    # Reconstruir el camino desde el nodo objetivo al nodo inicio
    def _reconstruir_camino(self, visitados, inicio, objetivo):
        camino = []
        nodo = objetivo
        while nodo is not None:
            camino.append(nodo)
            nodo = visitados[nodo]
        camino.reverse()
        
        return camino

# Grafo representado como un diccionario (lista de adyacencia)
system('cls')
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

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

# Crear el objeto BusquedaGrafo
busqueda = BusquedaGrafo(grafo)

# Ejemplo de búsqueda en anchura
system('cls')
camino_bfs = busqueda.busqueda_anchura(nodo_inicio, nodo_final)
print(f"Camino encontrado con BFS: {camino_bfs}")