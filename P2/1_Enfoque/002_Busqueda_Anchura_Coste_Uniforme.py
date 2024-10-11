import heapq
from os import system

# Función para realizar la búsqueda en anchura de costo uniforme
def bfs_costo_uniforme(grafo, inicio, objetivo):
    # Cola de prioridad (heap) para explorar los nodos
    cola_prioridad = [(0, inicio)]  # (costo_acumulado, nodo)
    # Diccionario para registrar los costos mínimos hasta cada nodo
    costos = {inicio: 0}
    # Diccionario para registrar el camino más corto
    padres = {inicio: None}
    
    while cola_prioridad:
        # Extraer el nodo con el costo acumulado más bajo
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si hemos alcanzado el nodo objetivo, podemos detenernos
        if nodo_actual == objetivo:
            print(f"Objetivo {objetivo} alcanzado con costo {costo_actual}")
            return reconstruir_camino(padres, inicio, objetivo)

        # Explorar los vecinos del nodo
        for vecino, costo_arco in grafo[nodo_actual]:
            nuevo_costo = costo_actual + costo_arco
            # Si encontramos un camino más barato hacia el vecino, lo actualizamos
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                padres[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino))

    return None  # Si no se encuentra un camino al objetivo

# Función para reconstruir el camino desde el nodo inicio al objetivo
def reconstruir_camino(padres, inicio, objetivo):
    camino = []
    nodo = objetivo
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()  # Invertimos la lista para obtener el camino desde inicio a objetivo
    return camino

# Grafo ponderado (diccionario donde cada nodo apunta a una lista de tuplas (vecino, costo))
system('cls')
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 1)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 1), ('E', 1)]
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

# Llamada a la función BFS de costo uniforme, buscando el camino desde 'x' hasta 'y'
system('cls')
camino = bfs_costo_uniforme(grafo, nodo_inicio, nodo_final)
print(f"Camino más corto de {nodo_inicio} a {nodo_final} es: {camino}")
