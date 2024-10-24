import numpy as np
from os import system

# Datos de ejemplo: cada documento representado por la presencia (1) o ausencia (0) de palabras
# Columnas: ["palabra_1", "palabra_2", "palabra_3"]
# Clases: 0 = "no spam", 1 = "spam"
X = np.array([
    [1, 0, 1],  # Documento 1
    [1, 1, 1],  # Documento 2
    [0, 0, 1],  # Documento 3
    [0, 1, 0],  # Documento 4
    [1, 0, 0]   # Documento 5
])

y = np.array([1, 1, 0, 0, 1])  # Etiquetas

# Función para calcular las probabilidades
def train_naive_bayes(X, y):
    n_samples, n_features = X.shape
    n_classes = len(np.unique(y))
    
    # Probabilidad previa
    priors = np.zeros(n_classes)
    
    # Probabilidades de verosimilitud
    likelihoods = np.zeros((n_classes, n_features))
    
    for c in range(n_classes):
        X_c = X[y == c]  # Filtrar los ejemplos de la clase c
        priors[c] = X_c.shape[0] / n_samples  # P(C)
        likelihoods[c, :] = (X_c.sum(axis=0) + 1) / (X_c.shape[0] + 2)  # P(X|C) con suavizado de Laplace
    
    return priors, likelihoods

# Función para clasificar nuevos ejemplos
def predict_naive_bayes(priors, likelihoods, X):
    n_samples = X.shape[0]
    n_classes = len(priors)
    predictions = np.zeros(n_samples)
    
    for i in range(n_samples):
        posteriors = np.zeros(n_classes)
        for c in range(n_classes):
            # Calcular la probabilidad posterior
            posteriors[c] = priors[c] * np.prod(likelihoods[c, :] ** X[i]) * np.prod((1 - likelihoods[c, :]) ** (1 - X[i]))
        
        # Elegir la clase con la probabilidad posterior más alta
        predictions[i] = np.argmax(posteriors)
    
    return predictions

# Entrenamiento del clasificador
priors, likelihoods = train_naive_bayes(X, y)

# Nuevos documentos para clasificar
new_documents = np.array([[1, 1, 0], [0, 0, 1],[1, 1, 1], [0, 0, 0]])
predictions = predict_naive_bayes(priors, likelihoods, new_documents)

# Mostrar resultados
system('cls')
for doc, pred in zip(new_documents, predictions):
    print(f"Documento: {doc}, Predicción: {'spam' if pred == 1 else 'no spam'}")
