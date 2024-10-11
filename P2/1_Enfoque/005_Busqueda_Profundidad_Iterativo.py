from os import system

# Función para realizar la búsqueda en profundidad iterativa
def dfs_iterativo(grafo, inicio):
    # Pila para explorar los nodos
    pila = [inicio]
    # Conjunto para marcar los nodos visitados
    visitados = set()

    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            print(nodo, end=" ")  # Procesar el nodo actual (imprimir en este caso)
            visitados.add(nodo)
            # Agregar los vecinos no visitados a la pila
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)

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

# Llamada a la función DFS, comenzando desde el nodo 'x'
system('cls')
print(f"El resultado de la búsqueda de anchura iniciando en el nodo {nodo} es:")
dfs_iterativo(grafo, nodo)