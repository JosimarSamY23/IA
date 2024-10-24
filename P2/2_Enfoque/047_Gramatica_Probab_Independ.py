import random
from os import system

# Definición de una gramática probabilística independiente del contexto (PCFG)
gramatica = {
    'S': [('NP VP', 1.0)],
    'NP': [('Det N', 0.8), ('N', 0.2)],
    'VP': [('V NP', 0.6), ('V', 0.4)],
    'Det': [('el', 0.5), ('la', 0.5)],
    'N': [('gato', 0.4), ('perro', 0.4), ('niño', 0.2)],
    'V': [('corre', 0.4), ('ladra', 0.3), ('duerme', 0.3)]
}

# Función para elegir una regla de producción basada en su probabilidad
def elegir_produccion(producciones):
    rand = random.random()
    acum = 0.0
    for produccion, probabilidad in producciones:
        acum += probabilidad
        if rand <= acum:
            return produccion
    return producciones[-1][0]

# Función para generar una oración a partir de la gramática
def generar_oracion(simbolo):
    if simbolo not in gramatica:
        return simbolo
    produccion = elegir_produccion(gramatica[simbolo])
    return ' '.join(generar_oracion(s) for s in produccion.split())

# Generar una oración a partir del símbolo inicial 'S' (oración completa)
system('cls')
oracion_generada = generar_oracion('S')
print("Oración generada:", oracion_generada)
