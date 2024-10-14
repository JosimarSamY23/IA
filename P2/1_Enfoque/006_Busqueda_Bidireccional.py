from collections import deque
from os import system

# Función para realizar la búsqueda bidireccional
def busqueda_bidireccional(grafo, inicio, objetivo):
    # Si el nodo inicio es igual al nodo objetivo, no necesitamos buscar
    if inicio == objetivo:
        return [inicio]

    # Colas para las búsquedas desde el inicio y el objetivo
    cola_inicio = deque([inicio])
    cola_objetivo = deque([objetivo])

    # Conjuntos para los nodos visitados desde el inicio y desde el objetivo
    visitados_inicio = {inicio: None}
    visitados_objetivo = {objetivo: None}

    while cola_inicio and cola_objetivo:
        # Expandir desde el lado del inicio
        if _expandir_nivel(grafo, cola_inicio, visitados_inicio, visitados_objetivo):
            return _reconstruir_camino(visitados_inicio, visitados_objetivo, cola_inicio[0])

        # Expandir desde el lado del objetivo
        if _expandir_nivel(grafo, cola_objetivo, visitados_objetivo, visitados_inicio):
            return _reconstruir_camino(visitados_inicio, visitados_objetivo, cola_objetivo[0])

    # Si no se encuentran las búsquedas, no hay camino
    return None

# Función para expandir un nivel en la búsqueda
def _expandir_nivel(grafo, cola, visitados, visitados_contrario):
    # Extraer el nodo del frente de la cola
    nodo_actual = cola.popleft()

    # Explorar sus vecinos
    for vecino in grafo[nodo_actual]:
        if vecino not in visitados:
            # Marcar como visitado desde este lado
            visitados[vecino] = nodo_actual
            cola.append(vecino)

            # Si el vecino ya fue visitado desde el otro lado, se encontró un encuentro
            if vecino in visitados_contrario:
                return True

    return False

# Función para reconstruir el camino desde las búsquedas en ambos lados
def _reconstruir_camino(visitados_inicio, visitados_objetivo, punto_encuentro):
    # Reconstruir el camino desde el inicio hasta el punto de encuentro
    camino_inicio = []
    nodo = punto_encuentro
    
    while nodo is not None:
        camino_inicio.append(nodo)
        nodo = visitados_inicio[nodo]
    camino_inicio.reverse()

    # Reconstruir el camino desde el objetivo hasta el punto de encuentro
    camino_objetivo = []
    nodo = visitados_objetivo[punto_encuentro]

    # Evitar ciclos: asegurarse de que no se repitan nodos ya visitados
    while nodo is not None and nodo not in camino_inicio:
        camino_objetivo.append(nodo)
        nodo = visitados_objetivo[nodo]

    # Combinar ambos caminos
    return camino_inicio + camino_objetivo


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

# Llamada a la función de búsqueda bidireccional, buscando el camino de 'x' a 'y'
system('cls')
camino = busqueda_bidireccional(grafo, nodo_inicio, nodo_final)
print(f"Camino encontrado: {camino}")
