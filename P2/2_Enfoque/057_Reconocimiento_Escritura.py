import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from os import system

# Cargar el conjunto de datos MNIST
mnist = keras.datasets.mnist

# Dividir el conjunto de datos en entrenamiento y prueba
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos a un rango de 0 a 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Definir el modelo
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Aplana las imágenes de 28x28 a 784
    layers.Dense(128, activation='relu'),   # Capa oculta con 128 neuronas
    layers.Dense(10, activation='softmax')  # Capa de salida para 10 clases (dígitos del 0 al 9)
])

# Compilar el modelo
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nPrecisión en el conjunto de prueba: {test_acc}')

# Función para predecir un dígito
def predecir_digito(imagen):
    imagen = imagen.reshape(1, 28, 28)  # Ajustar la forma de la imagen
    predicciones = model.predict(imagen)
    return np.argmax(predicciones)

# Probar el modelo con una imagen del conjunto de prueba
system('cls')
index = 0  # Cambia el índice para probar otras imágenes
digito = x_test[index]
plt.imshow(digito, cmap='gray')
plt.title(f'Dígito real: {y_test[index]}')
plt.show()

# Realizar la predicción
prediccion = predecir_digito(digito)
print(f'Predicción del modelo: {prediccion}')