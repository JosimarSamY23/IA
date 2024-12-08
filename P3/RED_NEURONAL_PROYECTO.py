#Introducción al aprendizaje profundo: conceptos básicos de aprendizaje profundo con Python, TensorFlow y Keras
#Samuel Josimar Orozco Torres 21110380 6E2

from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
from google.colab import files
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargamos el dataset de Mnist, digitos del 0-9 de 28x28 píxeles
mnist = keras.datasets.mnist
#X es para entrenamiento y prueba de imágenes.
#Y es para entrenamiento y prueba de etiquetado.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los datos, escalamos de 0 - 255 a 0 - 1
x_train = x_train.astype('float32') / 255.0
x_test  = x_test.astype('float32') / 255.0

# 2. Definir el modelo
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

#Capa de entrada
#Capa oculta con 128 neuronas con activación ReLU para introducir no linealidad.
#Capa de salida con 10 neuronas, una capa por cada clase, en este caso por cada dígito, del 0 - 9 con activación softmax para producir probabilidades.

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#Adam, optimizador que ajusta los pesos del modelo.
#Función de pérdida.
#Métrica para medir el desempeño.

# 3. Entrenar el modelo con los datos  de entrenamiento durante 7 épocas.
model.fit(x_train, y_train, epochs=7)

# 4. Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nPrecisión en el conjunto de prueba: {test_acc}')

#Valor de la función de pérdida.
#Precisión del modelo.

# 5. Subir una imagen desde la computadora
print("Por favor, sube una imagen (28x28 píxeles, escala de grises).")
uploaded = files.upload()
ruta_imagen = list(uploaded.keys())[0]

# 6. Función para predecir un dígito de una imagen personalizada
def predecir_imagen_personalizada(ruta_imagen):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen).convert('L')  # Convertir a escala de grises
    imagen = imagen.resize((28, 28))  # Redimensionar a 28x28

    # Convertir a array de numpy y normalizar
    imagen_array = np.array(imagen).astype('float32') / 255.0

    # Invertir colores si es necesario
    if np.mean(imagen_array) > 0.5:  # Suponiendo que el fondo debería ser negro
        imagen_array = 1 - imagen_array

    # Ajustar forma para el modelo
    imagen_array = imagen_array.reshape(1, 28, 28)

    # Realizar la predicción
    prediccion = model.predict(imagen_array)  #Obtebnemos las probabilidades de las clases
    digito_predicho = np.argmax(prediccion)   # Devuelve el índice de la clase con mayor probabilidad.

    # Visualizar la imagen
    plt.imshow(imagen_array.reshape(28, 28), cmap='gray')
    plt.title(f'Predicción del modelo: {digito_predicho}')
    plt.show()

    return digito_predicho

# 7. Probar el modelo con la imagen subida
digito_predicho = predecir_imagen_personalizada(ruta_imagen)
print(f'El modelo predice que el dígito es: {digito_predicho}')