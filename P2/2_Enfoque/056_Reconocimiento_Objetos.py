import cv2
from os import system

# Cargar el clasificador Haar Cascade preentrenado para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen
imagen = cv2.imread('056_Ejemplo.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises

# Detección de rostros
rostros = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar rectángulos alrededor de los rostros detectados
for (x, y, w, h) in rostros:
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Rectángulo en azul

# Mostrar la imagen con las detecciones
system('cls')
cv2.imshow("Detección de Rostros", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()