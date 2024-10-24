import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from os import system

# Colección de documentos (base de datos)
documentos = [
    "El gato persigue al ratón",
    "El perro ladra en el parque",
    "El ratón come queso en la cocina",
    "El gato duerme en la cama",
    "El perro persigue la pelota",
    "El gato juega con el ratón"
]

# Función para recuperar los documentos más relevantes para una consulta
def recuperar_documentos(consulta, documentos):
    # Convertir la colección de documentos y la consulta en una matriz de TF-IDF
    vectorizador = TfidfVectorizer()
    tfidf_documentos = vectorizador.fit_transform(documentos)
    
    # Convertir la consulta en un vector de TF-IDF utilizando el mismo vectorizador
    tfidf_consulta = vectorizador.transform([consulta])
    
    # Calcular la similitud del coseno entre la consulta y los documentos
    similitudes = cosine_similarity(tfidf_consulta, tfidf_documentos).flatten()
    
    # Obtener los índices de los documentos ordenados por relevancia (similitud más alta primero)
    indices_ordenados = np.argsort(similitudes)[::-1]
    
    # Mostrar los documentos más relevantes
    print(f"\nConsulta: '{consulta}'\n")
    for indice in indices_ordenados:
        print(f"Documento {indice + 1} (Similitud: {similitudes[indice]:.4f}): {documentos[indice]}")

# Consulta del usuario
system('cls')
consulta_usuario = "gato persigue ratón"

# Recuperar los documentos más relevantes para la consulta
recuperar_documentos(consulta_usuario, documentos)