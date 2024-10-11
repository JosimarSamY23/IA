from os import system

# Función para realizar la búsqueda en profundidad
def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()  # Conjunto para marcar los nodos visitados

    # Marcar el nodo actual como visitado
    visitados.add(inicio)
    print(inicio, end=" ")  # Procesar el nodo (imprimir en este caso)

    # Explorar recursivamente los vecinos no visitados
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

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
dfs(grafo, nodo)
