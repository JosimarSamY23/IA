import cv2
from os import system

# Captura de video (0 para la cámara web o la ruta de un archivo de video)
captura = cv2.VideoCapture(0)

# Leer el primer cuadro (fotograma) y convertirlo a escala de grises
ret, cuadro_anterior = captura.read()
cuadro_anterior = cv2.cvtColor(cuadro_anterior, cv2.COLOR_BGR2GRAY)
cuadro_anterior = cv2.GaussianBlur(cuadro_anterior, (21, 21), 0)

system('cls')
while True:
    # Leer el siguiente cuadro
    ret, cuadro_actual = captura.read()
    if not ret:
        break

    # Convertir el cuadro a escala de grises y aplicar desenfoque
    cuadro_gris = cv2.cvtColor(cuadro_actual, cv2.COLOR_BGR2GRAY)
    cuadro_gris = cv2.GaussianBlur(cuadro_gris, (21, 21), 0)

    # Calcular la diferencia entre el cuadro anterior y el cuadro actual
    diferencia = cv2.absdiff(cuadro_anterior, cuadro_gris)

    # Aplicar un umbral para obtener una imagen binaria (donde hay movimiento)
    _, umbral = cv2.threshold(diferencia, 25, 255, cv2.THRESH_BINARY)

    # Dilatar la imagen para cubrir huecos en los objetos detectados
    umbral = cv2.dilate(umbral, None, iterations=2)

    # Encontrar los contornos en la imagen umbralizada
    contornos, _ = cv2.findContours(umbral.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos detectados
    for contorno in contornos:
        if cv2.contourArea(contorno) < 500:  # Ignorar pequeños movimientos
            continue
        (x, y, w, h) = cv2.boundingRect(contorno)
        cv2.rectangle(cuadro_actual, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el cuadro con el movimiento detectado
    cv2.imshow('Movimiento', cuadro_actual)

    # Actualizar el cuadro anterior para la siguiente iteración
    cuadro_anterior = cuadro_gris

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
captura.release()
cv2.destroyAllWindows()
