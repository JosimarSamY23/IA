import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from os import system

# Cargar el dataset Iris
iris = datasets.load_iris()
X = iris.data[:, :2]  # Solo usaremos las dos primeras características para la visualización
y = iris.target

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador SVM con núcleo RBF
svm_model = SVC(kernel='rbf', gamma='scale')  # 'scale' es el valor por defecto

# Entrenar el modelo
svm_model.fit(X_train, y_train)

# Predecir las etiquetas del conjunto de prueba
y_pred = svm_model.predict(X_test)

# Mostrar la precisión
accuracy = np.mean(y_pred == y_test)
print(f"Precisión de SVM: {accuracy:.2f}")

# Visualizar el resultado
h = .02  # Paso en el espacio de características

# Crear una malla de puntos
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predecir la clase para cada punto en la malla
Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Graficar los resultados
system('cls')
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', marker='o', label='Entrenamiento')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', marker='x', label='Prueba')
plt.title("SVM con núcleo RBF")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()
