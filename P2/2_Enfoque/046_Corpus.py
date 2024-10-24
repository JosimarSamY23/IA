import random
from collections import defaultdict
from os import system

# Función para generar n-gramas de un corpus
def generar_ngrams(corpus, n):
    ngrams = defaultdict(list)
    palabras = corpus.split()
    for i in range(len(palabras) - n):
        key = tuple(palabras[i:i+n-1])
        siguiente_palabra = palabras[i+n-1]
        ngrams[key].append(siguiente_palabra)
    return ngrams

# Función para generar una oración usando el modelo de n-gramas
def generar_oracion(ngrams, longitud):
    start = random.choice(list(ngrams.keys()))
    oracion = list(start)
    for _ in range(longitud - len(start)):
        siguiente_palabra = random.choice(ngrams[tuple(oracion[-(len(start)):])])
        oracion.append(siguiente_palabra)
    return ' '.join(oracion)

# Ejemplo de corpus
corpus = """el gato negro corre rápido por el tejado
            el perro marrón ladra fuerte bajo la lluvia
            el gato gris duerme en el sillón de la sala"""

# Generar un modelo de 3-gramas (trigramas)
ngrams = generar_ngrams(corpus, 3)

# Generar una oración basada en el modelo de trigramas
system('cls')
oracion_generada = generar_oracion(ngrams, 10)
print("Oración generada:", oracion_generada)
