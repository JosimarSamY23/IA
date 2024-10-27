from os import system
import time

def cargar_preguntas(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read().strip().split('\n\n')
        preguntas = []

        for bloque in contenido:
            lineas = bloque.split('\n')
            texto_pregunta = lineas[0]
            opciones = lineas[1:4]
            respuesta_correcta = lineas[4].split(': ')[1]

            preguntas.append({
                'pregunta': texto_pregunta,
                'opciones': opciones,
                'respuesta': respuesta_correcta
            })

        return preguntas

def ejecutar_quiz(preguntas):
    puntaje = 0

    for i, pregunta in enumerate(preguntas):
        print(f"{pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)

        respuesta_usuario = input("Tu respuesta: ").strip().lower()

        if respuesta_usuario == pregunta['respuesta']:
            print("Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta es {pregunta['respuesta']}")
        
        print()
        time.sleep(2)
        system('cls')

    print(f"Tu puntaje final es {puntaje}/{len(preguntas)}")

# Ejecutar el quiz
system('cls')
preguntas = cargar_preguntas('004_Preguntas.txt')
ejecutar_quiz(preguntas)
