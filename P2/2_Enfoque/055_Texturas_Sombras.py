import cv2
import numpy as np
import matplotlib.pyplot as plt
from os import system

# Cargar la imagen
imagen = cv2.imread('055_Ejemplo.jpg')
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir a RGB para mostrar con Matplotlib

# Detección de texturas utilizando el filtro Sobel
sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=5)  # Filtro Sobel en la dirección x
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=5)  # Filtro Sobel en la dirección y
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)  # Magnitud de los bordes

# Normalizar la magnitud para que los valores estén entre 0 y 255
sobel_magnitude = cv2.normalize(sobel_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Crear una sombra sobre la imagen
# Crear una máscara para la sombra (puedes ajustar la intensidad y el área)
sombra = np.zeros_like(imagen_rgb)
height, width = imagen_rgb.shape[:2]
sombra[int(height * 0.5):, int(width * 0.5):] = [50, 50, 50]  # Sombra en la parte inferior derecha

# Combinar la imagen con la sombra
imagen_con_sombra = cv2.addWeighted(imagen_rgb, 1, sombra, 0.5, 0)

# Mostrar los resultados
system('cls')
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(imagen_rgb)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel_magnitude, cmap='gray')
plt.title('Detección de Textura (Sobel)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(imagen_con_sombra)
plt.title('Imagen con Sombra')
plt.axis('off')

plt.tight_layout()
plt.show()
