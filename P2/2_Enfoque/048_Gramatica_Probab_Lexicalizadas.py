import random
from os import system

# Definición de una gramática probabilística lexicalizada
gramatica_lexicalizada = {
    'S': [(('NP', 'VP'), None, 1.0)],
    'NP': [(('Det', 'N'), 'gato', 0.4), (('Det', 'N'), 'perro', 0.6)],
    'VP': [(('V', 'NP'), None, 0.5), (('V', 'NP'), None, 0.5)],
    'Det': [('el', None, 0.7), ('la', None, 0.3)],
    'N': [('gato', None, 0.5), ('perro', None, 0.5)],
    'V': [('corre', None, 0.5), ('ladra', None, 0.5)]
}

# Función para elegir una producción basada en su probabilidad
def elegir_produccion(producciones):
    rand = random.random()
    acum = 0.0
    for produccion, _, probabilidad in producciones:
        acum += probabilidad
        if rand <= acum:
            return produccion
    return producciones[-1][0]

# Función para elegir una palabra léxica asociada a una producción
def elegir_palabra(producciones):
    rand = random.random()
    acum = 0.0
    for _, palabra, probabilidad in producciones:
        acum += probabilidad
        if rand <= acum:
            return palabra
    return producciones[-1][1]

# Función para generar una oración a partir de la gramática lexicalizada
def generar_oracion(simbolo):
    if simbolo not in gramatica_lexicalizada:
        return simbolo
    
    producciones = gramatica_lexicalizada[simbolo]
    
    if simbolo == 'NP':  # Si es NP, elegir una palabra léxica
        palabra = elegir_palabra(producciones)
        return palabra
    
    produccion = elegir_produccion(producciones)
    
    return ' '.join(generar_oracion(s) for s in produccion)

# Generar una oración a partir del símbolo inicial 'S'
system('cls')
oracion_generada = generar_oracion('S')
print("Oración generada:", oracion_generada)