import cv2
from os import system

# Cargar una imagen
imagen = cv2.imread('007_Ejemplo.png')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes utilizando el algoritmo de Canny
bordes = cv2.Canny(imagen_gris, 100, 200)

# Mostrar la imagen original y la imagen con bordes detectados
system('cls')
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Bordes Detectados', bordes)

# Esperar una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()