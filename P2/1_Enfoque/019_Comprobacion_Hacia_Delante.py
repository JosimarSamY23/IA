# Resolver el problema de las N-Reinas usando forward checking

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

def forward_checking(tablero, col, N, dominios):
    # Si todas las reinas están colocadas, se ha encontrado una solución
    if col >= N:
        return True

    # Para cada fila en la columna actual
    for fila in dominios[col]:
        if es_seguro(tablero, fila, col, N):
            # Colocar la reina
            tablero[fila][col] = 1

            # Crear una copia de los dominios
            nuevos_dominios = [list(d) for d in dominios]

            # Actualizar los dominios para las columnas futuras
            for c in range(col + 1, N):
                if fila in nuevos_dominios[c]:
                    nuevos_dominios[c].remove(fila)  # Eliminar fila en conflicto
                diagonal1 = fila + (c - col)
                diagonal2 = fila - (c - col)
                if diagonal1 in nuevos_dominios[c]:
                    nuevos_dominios[c].remove(diagonal1)  # Eliminar diagonal superior
                if diagonal2 in nuevos_dominios[c]:
                    nuevos_dominios[c].remove(diagonal2)  # Eliminar diagonal inferior

            # Si algún dominio está vacío, retroceder
            if all(nuevos_dominios[c] for c in range(col + 1, N)):
                # Recursión con la siguiente columna
                if forward_checking(tablero, col + 1, N, nuevos_dominios):
                    return True

            # Si la colocación no lleva a una solución, quitar la reina
            tablero[fila][col] = 0

    # Si no se puede colocar una reina en esta columna, retroceder
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

# Inicializar los dominios: inicialmente, cualquier fila es válida para cada columna
dominios = [list(range(N)) for _ in range(N)]

# Intentar resolver el problema
if forward_checking(tablero, 0, N, dominios):
    print(f"Solución encontrada para {N} reinas:")
    imprimir_tablero(tablero, N)
else:
    print(f"No se encontró solución para {N} reinas.")
