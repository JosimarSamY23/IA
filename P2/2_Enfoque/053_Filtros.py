import cv2
import matplotlib.pyplot as plt
from os import system

# Cargar la imagen
imagen = cv2.imread('053_Ejemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar un filtro de desenfoque gaussiano
filtro_gaussiano = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicar el filtro de detección de bordes de Canny
filtro_canny = cv2.Canny(imagen, 100, 200)

# Aplicar un filtro de suavizado bilateral
filtro_bilateral = cv2.bilateralFilter(imagen, 9, 75, 75)

# Mostrar los resultados
imagenes = [imagen, filtro_gaussiano, filtro_canny, filtro_bilateral]
titulos = ['Original', 'Filtro Gaussiano', 'Filtro Canny', 'Filtro Bilateral']

system('cls')
plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
