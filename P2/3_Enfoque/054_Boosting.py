import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generacion de un conjunto de datos de ejemplo
X, y = make_classification(n_samples=200, n_features=10, n_informative=5, n_redundant=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializacion del clasificador base
clasificador_base = DecisionTreeClassifier(max_depth=1)

# Construccion del modelo AdaBoost con 50 clasificadores debiles
modelo_boosting = AdaBoostClassifier(n_estimators=50, random_state=42)

# Entrenamiento del modelo con el clasificador base
modelo_boosting.fit(X_train, y_train)

# Prediccion en el conjunto de prueba
y_pred = modelo_boosting.predict(X_test)

# Calculo de la precision del modelo
precision = accuracy_score(y_test, y_pred)
print("Precision del modelo AdaBoost: {:.2f}%".format(precision * 100))