import random
from collections import defaultdict
from os import system

# Datos de ejemplo (corpus)
corpus = [
    "el gato está en el jardín",
    "el perro juega en el jardín",
    "el gato duerme en la casa",
    "el perro ladra en la casa",
    "el gato juega con el perro"
]

# Preprocesar el corpus y dividir en bi-gramas
def generar_bi_gramas(corpus):
    bigramas = defaultdict(lambda: defaultdict(int))
    for frase in corpus:
        palabras = frase.split()
        for i in range(len(palabras) - 1):
            bigramas[palabras[i]][palabras[i+1]] += 1
    return bigramas

# Normalizar para convertir en probabilidades
def normalizar_bi_gramas(bigramas):
    modelo = defaultdict(dict)
    for palabra, siguiente_palabras in bigramas.items():
        total = sum(siguiente_palabras.values())
        for siguiente, cuenta in siguiente_palabras.items():
            modelo[palabra][siguiente] = cuenta / total
    return modelo

# Generar bigramas y normalizar
bigramas = generar_bi_gramas(corpus)
modelo_prob = normalizar_bi_gramas(bigramas)

# Generar texto a partir del modelo de bigramas
def generar_frase(modelo, palabra_inicial, longitud=5):
    palabra_actual = palabra_inicial
    frase = [palabra_actual]
    
    for _ in range(longitud - 1):
        palabra_siguiente = random.choices(
            list(modelo[palabra_actual].keys()), 
            list(modelo[palabra_actual].values())
        )[0]
        frase.append(palabra_siguiente)
        palabra_actual = palabra_siguiente
    
    return ' '.join(frase)

# Generar una frase comenzando con "el"
system('cls')
frase_generada = generar_frase(modelo_prob, "perro")
print("Frase generada:", frase_generada)
