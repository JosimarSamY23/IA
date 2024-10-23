# Problema de coloración de mapas con CSP

from os import system

# Definir las variables (regiones) y sus vecinos
variables = {
    'WA': ['NT', 'SA'], 
    'NT': ['WA', 'SA', 'Q'], 
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 
    'Q': ['NT', 'SA', 'NSW'], 
    'NSW': ['Q', 'SA', 'V'], 
    'V': ['SA', 'NSW'], 
    'T': []
}

# Definir el dominio (colores disponibles)
domain = {
    'WA': ['Red', 'Green', 'Blue'],
    'NT': ['Red', 'Green', 'Blue'],
    'SA': ['Red', 'Green', 'Blue'],
    'Q': ['Red', 'Green', 'Blue'],
    'NSW': ['Red', 'Green', 'Blue'],
    'V': ['Red', 'Green', 'Blue'],
    'T': ['Red', 'Green', 'Blue']
}

# Función que verifica si la asignación es consistente con las restricciones
def is_consistent(variable, value, assignment):
    for neighbor in variables[variable]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

# Algoritmo de backtracking
def backtrack(assignment):
    # Si la asignación está completa, devolverla
    if len(assignment) == len(variables):
        return assignment
    
    # Seleccionar una variable no asignada
    unassigned = [v for v in variables if v not in assignment]
    first = unassigned[0]

    # Intentar asignar un valor del dominio de la variable
    for value in domain[first]:
        if is_consistent(first, value, assignment):
            # Realizar la asignación
            assignment[first] = value
            
            # Llamada recursiva
            result = backtrack(assignment)
            
            # Si la asignación resultante es válida, devolverla
            if result is not None:
                return result
            
            # Si no es válida, deshacer la asignación
            assignment.pop(first)
    
    # Si no se encuentra una solución, devolver None
    return None

# Resolver el problema
system('cls')
solution = backtrack({})
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
