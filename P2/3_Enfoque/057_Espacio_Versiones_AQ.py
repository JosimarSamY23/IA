import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

class AQAlgorithm:
    def __init__(self):
        self.hipotesis = []

    def entrenar(self, X, y):
        for i in range(len(X)):
            if y[i] == 1:  # Solo consideramos ejemplos positivos
                self.agregar_version(X[i])

    def agregar_version(self, ejemplo):
        # Crear una nueva versión (regla) basada en el ejemplo
        nueva_version = set()
        for j in range(len(ejemplo)):
            nueva_version.add((j, ejemplo[j]))  # (índice de la característica, valor)
        self.hipotesis.append(nueva_version)

    def predecir(self, X):
        predicciones = []
        for ejemplo in X:
            if self.verificar_version(ejemplo):
                predicciones.append(1)
            else:
                predicciones.append(0)
        return predicciones

    def verificar_version(self, ejemplo):
        for version in self.hipotesis:
            if all(ejemplo[i] == valor for i, valor in version):
                return True
        return False

# Generar un conjunto de datos de clasificación
X, y = make_classification(n_samples=100, n_features=3, n_informative=2, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar y entrenar el algoritmo AQ
modelo_aq = AQAlgorithm()
modelo_aq.entrenar(X_train, y_train)

# Hacer predicciones
predicciones = modelo_aq.predecir(X_test)

# Calcular precisión
precision = np.mean(predicciones == y_test)
print(f"Precision del modelo AQ: {precision:.2f}")