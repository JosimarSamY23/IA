from os import system

# Corpus paralelo (pequeño ejemplo)
# Cada oración en español tiene su correspondiente traducción en inglés.
corpus_es = ["el gato está en la casa", "el perro está en el jardín", "la casa es grande"]
corpus_en = ["the cat is in the house", "the dog is in the garden", "the house is big"]

# Extraer pares de palabras (bigramas) entre los dos idiomas
def obtener_bigramas(oracion):
    palabras = oracion.split()
    bigramas = [(palabras[i], palabras[i+1]) for i in range(len(palabras)-1)]
    return bigramas

# Modelo de traducción básico basado en bigramas
def entrenar_modelo_traduccion(corpus_es, corpus_en):
    modelo_traduccion = {}
    for oracion_es, oracion_en in zip(corpus_es, corpus_en):
        bigramas_es = obtener_bigramas(oracion_es)
        bigramas_en = obtener_bigramas(oracion_en)
        for big_es, big_en in zip(bigramas_es, bigramas_en):
            modelo_traduccion[big_es] = big_en
    return modelo_traduccion

# Generar una traducción usando el modelo entrenado
def traducir_oracion(oracion, modelo_traduccion):
    bigramas_es = obtener_bigramas(oracion)
    traduccion = []
    for big_es in bigramas_es:
        if big_es in modelo_traduccion:
            traduccion.append(" ".join(modelo_traduccion[big_es]))
        else:
            traduccion.append("???")  # Marca las traducciones desconocidas
    return " ".join(traduccion)

# Entrenar el modelo de traducción
modelo_traduccion = entrenar_modelo_traduccion(corpus_es, corpus_en)

# Traducir una nueva oración
oracion_es = "el gato está en la casa"
oracion_traducida = traducir_oracion(oracion_es, modelo_traduccion)

system('cls')
print(f"Oración original: {oracion_es}")
print(f"Traducción generada: {oracion_traducida}")