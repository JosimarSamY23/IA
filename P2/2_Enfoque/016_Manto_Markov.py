from os import system

# Definir la estructura de una red bayesiana como un diccionario de adyacencias
red_bayesiana = {
    'A': ['B'],  # A es padre de B
    'B': ['C'],  # B es padre de C
    'C': [],     # C no tiene hijos
    'D': ['C'],  # D es padre de C
    'E': ['C']   # E es padre de C
}

# Inverso de la estructura para obtener padres de cada nodo
padres = {
    'A': [],
    'B': ['A'],
    'C': ['B', 'D', 'E'],
    'D': [],
    'E': []
}

def manto_de_markov(variable, red_bayesiana, padres):
    # Padres de la variable
    manto = set(padres[variable])
    
    # Hijos de la variable
    hijos = red_bayesiana[variable]
    manto.update(hijos)
    
    # Otros padres de sus hijos
    for hijo in hijos:
        manto.update(padres[hijo])
    
    # Remover la variable misma del manto
    if variable in manto:
        manto.remove(variable)
    
    return manto

# Ejemplo: Obtener el manto de Markov de la variable 'x'
system('cls')
while True:
    try:
        manto = input("Ingresa una variable (A-E): ").upper()
        if manto in red_bayesiana.keys():
            break
        else:
            print("Ingresa una opción dentro del rango")
    except Exception:
        print("Elige una opción válida")

manto_usuario = manto_de_markov(manto, red_bayesiana, padres)
system('cls')
print(f"Manto de Markov de {manto}: {manto_usuario}")