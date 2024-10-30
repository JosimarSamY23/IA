import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Generar un conjunto de datos de clasificación
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar la mejor hipotesis actual
mejor_hipotesis = None
mejor_precision = 0

# Probar diferentes profundidades para el arbol de decision
for profundidad in range(1, 11):
    # Crear el modelo con la profundidad actual
    modelo = DecisionTreeClassifier(max_depth=profundidad, random_state=42)
    
    # Entrenar el modelo
    modelo.fit(X_train, y_train)
    
    # Hacer predicciones en el conjunto de prueba
    y_pred = modelo.predict(X_test)
    
    # Calcular la precision
    precision = accuracy_score(y_test, y_pred)
    print(f"Profundidad: {profundidad}, Precision: {precision:.2f}")
    
    # Actualizar la mejor hipotesis si la precision es mayor
    if precision > mejor_precision:
        mejor_precision = precision
        mejor_hipotesis = modelo

print("\nLa mejor hipotesis encontrada tiene una precision de {:.2f}".format(mejor_precision))