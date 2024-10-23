from collections import deque
from os import system

# Definimos el problema de coloreo de mapas con 3 colores
# Variables: Regiones A, B, C, D, E
# Dominios: Colores {Rojo, Verde, Azul}
variables = ['A', 'B', 'C', 'D', 'E']
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul'],
    'D': ['Rojo', 'Verde', 'Azul'],
    'E': ['Rojo', 'Verde', 'Azul']
}

# Restricciones: Las regiones adyacentes no deben tener el mismo color
adyacencias = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Función para verificar si dos valores son consistentes
def es_consistente(valor1, valor2):
    return valor1 != valor2

# Algoritmo AC-3 para la propagación de restricciones
def ac3(variables, dominios, adyacencias):
    # Inicializar cola con todos los arcos (pares de variables adyacentes)
    cola = deque([(xi, xj) for xi in variables for xj in adyacencias[xi]])

    while cola:
        xi, xj = cola.popleft()

        # Intentar reducir el dominio de xi
        if reducir_dominio(xi, xj, dominios):
            # Si se reduce el dominio de xi, verificar los vecinos de xi
            if len(dominios[xi]) == 0:
                return False  # Fallo: dominio vacío
            for xk in adyacencias[xi]:
                if xk != xj:
                    cola.append((xk, xi))

    return True  # Los dominios son consistentes

# Función para reducir el dominio de xi basado en xj
def reducir_dominio(xi, xj, dominios):
    reducido = False
    for valor in dominios[xi][:]:
        # Si no existe ningún valor en xj que sea consistente con el valor en xi
        if not any(es_consistente(valor, val) for val in dominios[xj]):
            dominios[xi].remove(valor)
            reducido = True
    return reducido

# Resolver el problema de coloreo de mapas usando AC-3
system('cls')
if ac3(variables, dominios, adyacencias):
    print("Solución encontrada:")
    for variable in dominios:
        print(f"{variable}: {dominios[variable]}")
else:
    print("No se encontró una solución.")
