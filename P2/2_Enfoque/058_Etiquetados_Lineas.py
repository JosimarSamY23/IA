import cv2
import numpy as np
from os import system

def ver_imagen(titulo, imagen):
    cv2.imshow(titulo, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def dimensiones(imagen):
    m, n = imagen.shape
    return m, n

imagen = cv2.imread("058_Ejemplo.jpeg", 0)
kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

m, n = dimensiones(imagen)
filtro_y  = np.zeros_like(imagen, dtype=np.int16)
filtro_x  = np.zeros_like(imagen, dtype=np.int16)
resultado = np.zeros_like(imagen, dtype=np.int16)

for x in range(m-2):
    for y in range(n-2):
        res_y = np.sum(imagen[x:x+3, y:y+3] * kernel_y)
        res_x = np.sum(imagen[x:x+3, y:y+3] * kernel_x)

        if res_y > 100:
            filtro_y[x, y] = 255
        if res_x > 100:
            filtro_x[x, y] = 255

        resultado[x, y] = np.absolute(filtro_y[x, y]) + np.absolute(filtro_x[x, y])

resultado = np.clip(resultado, 0, 255).astype(np.uint8)

system('cls')
ver_imagen("Original  ", imagen)
ver_imagen("Horizontal", filtro_y.astype(np.uint8))
ver_imagen("Vertical  ", filtro_x.astype(np.uint8))
ver_imagen("Suma      ", resultado)
