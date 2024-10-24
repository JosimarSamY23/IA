import cv2
import numpy as np
import matplotlib.pyplot as plt
from os import system

# Cargar la imagen
imagen = cv2.imread('054_Ejemplo.jpg')
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir a RGB para mostrar con Matplotlib

# Detección de aristas con el algoritmo Canny
edges = cv2.Canny(imagen, 100, 200)

# Segmentación utilizando k-means
# Redimensionar la imagen a una lista de píxeles
pixel_values = imagen.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# Definir criterios y número de clusters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3  # Número de colores (clusters)
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convertir los centros de vuelta a uint8 y reconstruir la imagen segmentada
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(imagen.shape)

# Mostrar los resultados
system('cls')
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(imagen_rgb)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Detección de Aristas (Canny)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(segmented_image)
plt.title('Imagen Segmentada (k-means)')
plt.axis('off')

plt.tight_layout()
plt.show()
