import heapq
from os import system

# Representación de un nodo en el grafo
class Nodo:
    def __init__(self, nombre, heuristica):
        self.nombre = nombre
        self.heuristica = heuristica  # Heurística del nodo

    def __eq__(self, other):
        return self.nombre == other.nombre

    def __hash__(self):
        return hash(self.nombre)

# Función de búsqueda informada online (una variante de A*)
def busqueda_informada_online(grafo, nodo_inicio, nodo_final):
    # Inicializar la cola de prioridad (heap) y el conjunto de nodos visitados
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, nodo_inicio))  # (costo total, nodo)
    caminos = {nodo_inicio: [nodo_inicio]}  # Rutas hasta cada nodo visitado
    visitados = set()

    while cola_prioridad:
        # Extraer el nodo con el costo total más bajo
        costo_total, nodo_actual = heapq.heappop(cola_prioridad)

        # Si llegamos al nodo objetivo, devolvemos el camino
        if nodo_actual.nombre == nodo_final:
            return caminos[nodo_actual]

        visitados.add(nodo_actual)

        # Explorar los vecinos
        for vecino, costo in grafo[nodo_actual.nombre]:
            if vecino not in visitados:
                nuevo_costo_total = costo_total + costo
                heapq.heappush(cola_prioridad, (nuevo_costo_total + vecino.heuristica, vecino))
                caminos[vecino] = caminos[nodo_actual] + [vecino.nombre]

    return None  # Si no se encuentra el camino

# Grafo representado como un diccionario
system('cls')
grafo = {
    'A': [(Nodo('B', 2), 1), (Nodo('C', 4), 2)],
    'B': [(Nodo('D', 1), 2), (Nodo('E', 3), 1)],
    'C': [(Nodo('F', 1), 1)],
    'D': [],
    'E': [(Nodo('F', 0), 1)],
    'F': []
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

# Búsqueda informada online desde el nodo 'x' hasta el nodo 'y'
camino = busqueda_informada_online(grafo, Nodo(nodo_inicio, 0), nodo_final)
print(f"Camino encontrado: {camino}")
