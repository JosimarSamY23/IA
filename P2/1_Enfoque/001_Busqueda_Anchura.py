from collections import deque
from os import system

# Función para realizar la búsqueda en anchura
def bfs(grafo, inicio):
    # Cola para explorar los nodos
    cola = deque([inicio])
    # Conjunto para marcar los nodos visitados
    visitados = set([inicio])
    
    # Mientras haya nodos por explorar
    while cola:
        # Extraer el nodo en el frente de la cola
        nodo = cola.popleft()
        print(nodo, end=" ")  # Procesar el nodo actual (imprimir en este caso)
        
        # Explorar los vecinos del nodo
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)

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
        nodo = input("Selecciona el nodo en donde comenzar (A-F): ").upper()

        if nodo in grafo.keys():
            break
        else:
            print("Selecciona una opción dentro del rango")

except Exception:
    print("Ingresa una opción correcta")

# Llamada a la función BFS
system('cls')
print(f"El resultado de la búsqueda de anchura iniciando en el nodo {nodo} es:")
bfs(grafo, nodo)
