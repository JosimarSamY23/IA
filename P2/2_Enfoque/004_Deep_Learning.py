import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import numpy as np

# Cargar el dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesar los datos
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))  # Agregar la dimensión de canal (1 para imágenes en escala de grises)
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1))
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizar los valores de los píxeles (0 a 1)

# Crear el modelo de red neuronal profunda (DNN)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))  # Capa convolucional
model.add(layers.MaxPooling2D((2, 2)))  # Capa de max-pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Aplanar y agregar capas completamente conectadas
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))  # Capa completamente conectada
model.add(layers.Dense(10, activation='softmax'))  # Capa de salida para 10 clases (dígitos 0-9)

# Compilar el modelo
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nPrecisión en el conjunto de prueba: {test_acc}')
