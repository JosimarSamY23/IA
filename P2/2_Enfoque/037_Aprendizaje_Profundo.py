import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from os import system

# Cargar el conjunto de datos MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizar las imágenes
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Convertir las etiquetas a formato categórico
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Crear el modelo
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))   # Aplanar la imagen
model.add(Dense(128, activation='relu'))   # Capa oculta con 128 neuronas
model.add(Dense(10, activation='softmax')) # Capa de salida con 10 clases

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Pérdida: {loss:.4f}, Precisión: {accuracy:.4f}')

# Hacer predicciones
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)

# Visualizar algunas predicciones
system('cls')
plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i], cmap='gray')
    plt.title(f'Predicción: {predicted_classes[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show()
