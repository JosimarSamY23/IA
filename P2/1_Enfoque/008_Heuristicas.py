import heapq
from os import system

# Clase para implementar el algoritmo A*
class BusquedaHeuristica:
    def __init__(self, grafo, heuristica):
        self.grafo = grafo
        self.heuristica = heuristica

    # Implementación del algoritmo A*
    def busqueda_a_estrella(self, inicio, objetivo):
        # Colas de prioridad para nodos a explorar
        cola_prioridad = []
        heapq.heappush(cola_prioridad, (0, inicio))

        # Diccionarios para almacenar costos y rutas
        costo_acumulado = {inicio: 0}
        padres = {inicio: None}

        while cola_prioridad:
            # Extraer el nodo con menor costo f(n)
            costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

            # Si encontramos el objetivo, reconstruimos el camino
            if nodo_actual == objetivo:
                return self._reconstruir_camino(padres, inicio, objetivo)

            # Explorar vecinos
            for vecino, costo in self.grafo[nodo_actual]:
                nuevo_costo = costo_acumulado[nodo_actual] + costo

                # Si encontramos un camino más corto hacia el vecino
                if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                    costo_acumulado[vecino] = nuevo_costo
                    prioridad = nuevo_costo + self.heuristica[vecino]  # f(n) = g(n) + h(n)
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    padres[vecino] = nodo_actual

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

# Crear el objeto de búsqueda heurística
busqueda = BusquedaHeuristica(grafo, heuristica)

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

# Ejemplo de búsqueda A* desde el nodo 'x' hasta el nodo 'y'
system('cls')
camino_a_estrella = busqueda.busqueda_a_estrella(nodo_inicio, nodo_final)
print(f"Camino encontrado con A*: {camino_a_estrella}")
