from os import system

# Función para realizar la búsqueda en profundidad limitada
def dfs_limitado(grafo, inicio, objetivo, limite, profundidad=0, visitados=None):
    if visitados is None:
        visitados = set()  # Conjunto para marcar los nodos visitados

    # Marcar el nodo actual como visitado
    visitados.add(inicio)
    print(f"Visitando: {inicio}, Profundidad: {profundidad}")  # Mostrar el nodo y su profundidad actual

    # Si encontramos el objetivo, terminamos
    if inicio == objetivo:
        return True

    # Si la profundidad actual es igual al límite, no continuar profundizando
    if profundidad >= limite:
        return False

    # Explorar recursivamente los vecinos no visitados
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            if dfs_limitado(grafo, vecino, objetivo, limite, profundidad + 1, visitados):
                return True

    return False  # Si no se encuentra el objetivo dentro del límite de profundidad

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

# Llamada a la función DFS limitado con un límite de profundidad de 2, buscando desde 'A' hasta 'F'
limite = 2
encontrado = dfs_limitado(grafo, nodo_inicio, nodo_final, limite)
print(f"Objetivo encontrado: {encontrado}")
