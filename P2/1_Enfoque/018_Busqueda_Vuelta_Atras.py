# Resolver el problema de las N-Reinas usando backtracking

from os import system

def es_seguro(tablero, fila, col, N):
    # Verificar la fila hacia la izquierda
    for i in range(col):
        if tablero[fila][i] == 1:
            return False
    
    # Verificar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Verificar la diagonal inferior izquierda
    for i, j in zip(range(fila, N), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_n_reinas(tablero, col, N):
    # Caso base: si todas las reinas están colocadas
    if col >= N:
        return True
    
    # Intentar colocar una reina en cada fila de la columna actual
    for i in range(N):
        if es_seguro(tablero, i, col, N):
            # Colocar la reina en la fila i
            tablero[i][col] = 1
            
            # Recursión para colocar el resto de las reinas
            if resolver_n_reinas(tablero, col + 1, N):
                return True
            
            # Si la colocación de la reina en la fila i no lleva a una solución, retroceder
            tablero[i][col] = 0
    
    # Si no se puede colocar una reina en esta columna, devolver False
    return False

def imprimir_tablero(tablero, N):
    for i in range(N):
        for j in range(N):
            print("Q" if tablero[i][j] == 1 else ".", end=" ")
        print()

# Parámetro N (número de reinas y tamaño del tablero N x N)
system('cls')
while True:
    try:
        system('cls')
        N = input("Ingresa el número de Damas: ")# Puedes cambiar este valor para probar con otros tamaños de tablero

        if N.isdigit:
            N = int(N)
            break
        else:
            print("Ingresa un entero")

    except Exception:
        print("Ingresa un valor válido")

# Inicializar el tablero N x N con ceros
tablero = [[0 for _ in range(N)] for _ in range(N)]

# Intentar resolver el problema
if resolver_n_reinas(tablero, 0, N):
    print(f"Solución encontrada para {N} reinas:")
    imprimir_tablero(tablero, N)
else:
    print(f"No se encontró solución para {N} reinas.")
