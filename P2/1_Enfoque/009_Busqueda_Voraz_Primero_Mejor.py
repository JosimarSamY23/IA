import heapq
from os import system

# Clase para implementar la búsqueda voraz (Greedy Best-First Search)
class BusquedaVoraz:
    def __init__(self, grafo, heuristica):
        self.grafo = grafo
        self.heuristica = heuristica

    # Implementación del algoritmo Greedy Best-First Search
    def busqueda_voraz(self, inicio, objetivo):
        # Cola de prioridad para los nodos a explorar
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (self.heuristica[inicio], inicio))

        # Diccionario para almacenar la ruta recorrida
        padres = {inicio: None}

        # Conjunto de nodos visitados
        visitados = set()

        while cola_prioridad:
            # Extraer el nodo con menor valor h(n)
            _, nodo_actual = heapq.heappop(cola_prioridad)

            # Si encontramos el objetivo, reconstruimos el camino
            if nodo_actual == objetivo:
                return self._reconstruir_camino(padres, inicio, objetivo)

            visitados.add(nodo_actual)

            # Explorar los vecinos
            for vecino, _ in self.grafo[nodo_actual]:
                if vecino not in visitados:
                    padres[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (self.heuristica[vecino], vecino))

        return None  # Si no se encuentra el objetivo

    # Función para reconstruir el camino desde el nodo objetivo hasta el inicio
    def _reconstruir_camino(self, padres, inicio, objetivo):
        camino = []
        nodo = objetivo

        while nodo is not None:
            camino.append(nodo)
            nodo = padres[nodo]
        camino.reverse()

        return camino

# Grafo representado como un diccionario (lista de adyacencia con costos)
system('cls')
grafo = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 3), ('E', 1)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 3)],
    'E': [('B', 1), ('F', 1)],
    'F': [('C', 2), ('E', 1)]
}

# Heurística (distancia estimada desde cada nodo hasta el nodo objetivo 'F')
heuristica = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 5,
    'E': 1,
    'F': 0
}

# Crear el objeto de búsqueda voraz
busqueda = BusquedaVoraz(grafo, heuristica)

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

# Ejemplo de búsqueda Greedy Best-First desde el nodo 'x' hasta el nodo 'y'
system('cls')
camino_voraz = busqueda.busqueda_voraz(nodo_inicio, nodo_final)
print(f"Camino encontrado con Búsqueda Voraz: {camino_voraz}")
