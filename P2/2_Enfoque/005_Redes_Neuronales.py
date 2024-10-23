import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar el dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesar los datos
x_train = x_train.reshape((x_train.shape[0], 28*28))  # Convertir las imágenes 28x28 en vectores de 784 píxeles
x_test = x_test.reshape((x_test.shape[0], 28*28))
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizar los valores de los píxeles (0 a 1)

# Crear el modelo de red neuronal
model = models.Sequential()
model.add(layers.Dense(128, activation='relu', input_shape=(28*28,)))  # Capa densa con 128 neuronas
model.add(layers.Dense(64, activation='relu'))  # Capa densa con 64 neuronas
model.add(layers.Dense(10, activation='softmax'))  # Capa de salida con 10 neuronas (para 10 clases: dígitos 0-9)

# Compilar el modelo
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'\nPrecisión en el conjunto de prueba: {test_acc}')
