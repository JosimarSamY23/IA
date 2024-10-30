import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Generacion de un conjunto de datos de ejemplo
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, n_redundant=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# K-DL: Uso de K-Nearest Neighbors
k_neighbors = 5
knn = KNeighborsClassifier(n_neighbors=k_neighbors)
knn.fit(X_train, y_train)

# Prediccion usando K-DL
y_pred_knn = knn.predict(X_test)

# Calculo de la precision del modelo K-DL
precision_knn = accuracy_score(y_test, y_pred_knn)
print("Precision del modelo K-DL (KNN): {:.2f}%".format(precision_knn * 100))

# K-DT: Uso de un Arbol de Decision
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

# Prediccion usando K-DT
y_pred_dt = decision_tree.predict(X_test)

# Calculo de la precision del modelo K-DT
precision_dt = accuracy_score(y_test, y_pred_dt)
print("Precision del modelo K-DT (Decision Tree): {:.2f}%".format(precision_dt * 100))