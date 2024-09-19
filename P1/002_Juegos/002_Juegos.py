#Samuel Josimar Orozco Torres -> 21110380 -> 6E2
import os
import random
import time

os.system('cls')

#Funciones
def menu():
    print("\n\tBienvenido a YosiJuego selecciona una opción:")
    print("\t1. Adivina el número")
    print("\t2. Tres en raya")
    print("\t3. Deal or no deal")
    print("\t4. Simon dice")
    print("\t5. Ruleta")
    print("\t6. Veintiuno")
    print("\t0. Salir")

def seleccionar_opcion_menu():
    opcion_menu = input("Opción: ")

    if opcion_menu == '1':
        adivina_numero()

    elif opcion_menu == '2':
        gato()

    elif opcion_menu == '3':
        deal()

    elif opcion_menu == '4':
        simon_dice()

    elif opcion_menu == '5':
        ruleta()

    elif opcion_menu == '6':
        blackjack()

    elif opcion_menu == '0':
        return True
        
    else:
        mensajes(3)

    return False

def mensajes(tipo):
    if tipo == 1:
        print("Felicidades has ganado")
    elif tipo == 2:
        print("Lo siento has perdido")
    else:
        print("Ingresa una opción válida")
    
    limpiar_pantalla()
    
def limpiar_pantalla():
    input("Presione una tecla para continuar")
    os.system('cls')

#Funciones juego adivina el numero
def adivina_numero():
    os.system('cls')
    num = random.randint(0,100)
    num_usuario = 0
    contador    = 1

    while contador!=8:
        try:
            print("Encuentra el número de 1 - 100. Intento:",contador,"/7")
            num_usuario = int(input("Elige un número: "))

            if contador!=7:
                if num_usuario == num:
                    mensajes(1)
                    break
                elif num_usuario > num:
                    print("El número es menor")
                else:
                    print("El número es mayor")
            else:
                mensajes(2)
                print("El número era: ", str(num))

            contador+=1
            limpiar_pantalla()

        except ValueError:
            mensajes(3)
#---------------------------------

#Funciones juego tres en raya
def crear_tablero():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-"*6)

def verificar_ganador(tablero,turno):
    jugadores = ["X","O"]
    jugador = ""

    if turno:
        jugador = jugadores[0]
    else:
        jugador = jugadores[1]

    for i in range(3):
        #VERIFICA TODOS LOS ELEMENTOS DE LA FILA                #VERIFICA TODOS LOS ELEMENTOS DE LA COLUMNA
        if all([tablero[i][j] == jugador for j in range(3)]) or all([tablero[j][i] == jugador for j in range(3)]):
            return True
        
        if(tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador) or (tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador):
            return True
        
        return False
    
def tablero_lleno(tablero):
    if all([celda!= " " for fila in tablero for celda in fila]):
        return True
    
    return False

def posicion_numero(numero):
    if numero   == 1: return (0,0)
    elif numero == 2: return (0,1)
    elif numero == 3: return (0,2)
    elif numero == 4: return (1,0)
    elif numero == 5: return (1,1)
    elif numero == 6: return (1,2)
    elif numero == 7: return (2,0)
    elif numero == 8: return (2,1)
    elif numero == 9: return (2,2)

def gato():
    os.system('cls')
    tablero = crear_tablero()
    jugadores = ["X","O"]
    turno = True
    jugador_actual = 0
    print("Bienvenidos al juego del gato")

    while True:
        
        if turno: 
            jugador_actual = 0
        else:     
            jugador_actual = 1

        while True:
            try:
                os.system('cls')
                print("Turno Jugador"+str(jugador_actual+1))
                imprimir_tablero(tablero)
                opc_jugador = int(input("Elige la posicion del 1-9: "))
                fila,columna = posicion_numero(opc_jugador)

                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugadores[jugador_actual]
                    break
                
                else:
                    print("La posición ya esta ocupada")
                    limpiar_pantalla()

            except (ValueError, IndexError, TypeError):
                mensajes(3)

        if verificar_ganador(tablero,turno):
            if turno: print("Ha ganado el jugador 1")
            else: print("Ha ganado el jugador 2")
            limpiar_pantalla()
            break

        if tablero_lleno(tablero):
            print("Es un empate")
            limpiar_pantalla()
            break

        turno = not turno
#---------------------------------

#Funiones juego deal or no deal
def deal():
    os.system('cls')
    valores_bajos = [1,5,10,50,100,250,500,750]
    valores_altos = [1000,2500,5000,10000,25000,50000,75000,100000]
    valores_maletines = valores_bajos + valores_altos
    random.shuffle(valores_maletines)

    maletin_usuario = []
    
    rondas = [4,3,3,2,1,1]
    ronda = 0
    lista_maletines_index = [(indice+1, valor) for indice, valor in enumerate(valores_maletines)]

    while True:
        print("\nMaletines")
        mostrar_valores(lista_maletines_index)
        print("\nEsccoge tu maletin. \n1)Eleccion \n2)Aleatorio")
        opcion = input("Opcion: ")

        if opcion=='1':
            while True:
                try:
                    aux_eleccion = int(input("Selecciona el maletín: "))

                    if 1 <= aux_eleccion <= len(lista_maletines_index):
                        maletin_usuario = lista_maletines_index[aux_eleccion-1]  # Agregamos un maletín
                        break
                    else:
                        print("Elige un número válido entre 1 y", len(lista_maletines_index))

                except ValueError:
                    mensajes(3)
                    
        elif opcion=='2':
            maletin_usuario = random.choice(lista_maletines_index)
            break

        else:
            mensajes(3)
            continue

        break
        
    indice_usuario, valor_usuario = maletin_usuario
    del lista_maletines_index[indice_usuario-1]
    limpiar_pantalla()

    print("Tu maletín es el número ",indice_usuario,"con un valor oculto.")

#Aqui vamos
    aux = 0
    while True:
        validar_juego = True

        for maletines in rondas:
            for maletin in range(maletines):
                while True:
                    print("Ronda: ",str(ronda+1))
                    print("\nMaletines disponibles: ")

                    mostrar_valores(lista_maletines_index)

                    print("\n\tValores bajos: ",valores_bajos)
                    print("\tValores altos: ",valores_altos)

                    print("\nMaletines por abrir: ",maletines)
                    print("Selecciona un maletin: ",str(maletin+1)," / ", str(maletines))
                    try:
                        numero_maletin = int(input("\tNumero de maletin: "))

                        if 1 <= numero_maletin <= 16:
                            contador = 0
                            for x in lista_maletines_index:
                                if x[0] == numero_maletin: #Entramos al valor del maletin
                                    break
                                contador+=1

                            indice, valor = lista_maletines_index[contador]
                            del lista_maletines_index[contador]

                            print("El maletin: ",indice," tiene el valor de: ",valor)
                            valores_bajos, valores_altos = eliminar_valor(valores_bajos, valores_altos,valor)
                            limpiar_pantalla()
                            break
                        else:
                            mensajes(3)
                        
                    except (ValueError, IndexError):
                        mensajes(3)

                aux +=1
                if aux == rondas[ronda]:
                    print("\n\tValores bajos: ",valores_bajos)
                    print("\tValores altos: ",valores_altos)
                    cifra_banco = llamada_banco(valores_bajos, valores_altos, valor_usuario)
                    print("\nEl banco hará una oferta...")
                    time.sleep(5)
                    print("El banco ofrece la cantidad de: ",cifra_banco)

                    opc_banco = input("Aceptas la oferta s/n: ")
                    if opc_banco == 's':
                        os.system('cls')
                        print("Felicidades, has ganado: ",cifra_banco)
                        limpiar_pantalla()
                        validar_juego = False
                        break

                    elif opc_banco == 'n':
                        print("Sigues en el juego")
                        limpiar_pantalla()

                    else:
                        mensajes(3)

                    ronda+=1
                    aux = 0

                    if ronda==6:
                        break

            if not validar_juego:
                break

            if ronda==6:
                break
        
        if not validar_juego:
            break

        #Al llegar a la ultima instancia
        print("\n\tValores bajos: ",valores_bajos)
        print("\tValores altos: ",valores_altos)

        print("¿Deseas quedarte con tu maletin?\n1)Si, quedarme con el.\n2)No, cambiar maletin")
        opc_ultima = input("\tOpcion: ")

        if opc_ultima == '1':
            print("Tu maletin <"+str(indice_usuario)+"> tiene la cantidad de: "+str(valor_usuario))
            mensajes(1)
            indice_usuario,valor_usuario = lista_maletines_index[0]
            print("En el maletin <"+str(indice_usuario)+"> habia la cantidad de: "+str(valor_usuario))
            limpiar_pantalla()
            break

        elif opc_ultima == '2':
            print("Tu maletin <"+str(indice_usuario)+"> tiene la cantidad de: "+str(valor_usuario))
            indice_usuario,valor_usuario = lista_maletines_index[0]
            print("En el maletin <"+str(indice_usuario)+"> has ganado la cantidad de: "+str(valor_usuario))
            limpiar_pantalla()
            break

        else:
            mensajes(3)

def eliminar_valor(lista1,lista2,valor):
    a1 = lista1
    b1 = lista2

    if valor in lista1:
        a1.remove(valor)

    if valor in lista2:
        b1.remove(valor)

    return a1,b1

def llamada_banco(bajos, altos, valor_usuario):
    aux1, aux2 = len(bajos), len(altos)
    aux3, aux4 = sum(bajos), sum(altos)

    if aux1 == 0:
        aux1 = 1
        aux3 =1

    if aux2 == 0:
        aux2 = 1
        aux4 = 1


    promedio_bajos = aux3 / aux1
    promedio_altos = aux4 / aux2
    peso_bajos = 1.5
    peso_altos = 1

    promedio_total = (promedio_bajos * peso_bajos + promedio_altos * peso_altos) / (peso_bajos + peso_altos)
    promedio_total = int(promedio_total)

    suerte = random.randint(0,1)
    
    return promedio_total
    

def mostrar_valores(lista):
    maletines_disponibles = [tupla[0] for tupla in lista]
    print(maletines_disponibles)
#---------------------------------

#Funiones juego simon dice
def mostrar_secuencia(secuencia):
    for numero in secuencia:
        print(numero, end=' <-> ', flush=True)
        time.sleep(2)
    
    os.system('cls')

def simon_dice():
    os.system('cls')
    print("¡Bienvenido a Yosi Dice!")
    secuencia = [] 
    ronda = 1 

    while True:
        nuevo_numero = random.randint(1, 5)
        secuencia.append(nuevo_numero)

        print("Ronda: ",ronda)
        mostrar_secuencia(secuencia)

        for i in range(ronda):
            while True:
                try:
                    print("¿Cual era el número "+str(i+1)+" ?")
                    respuesta_usuario = int(input("Repite el número: "))
                    if respuesta_usuario == secuencia[i]:
                        print("Correcto!")
                        break
                    else:
                        print("Incorrecto")
                        mensajes(2)
                        return
                    
                except ValueError:
                    mensajes(3)

        ronda += 1
#---------------------------------

#Funiones juego ruleta
def crear_ruleta():
    verde  = [(0,   'verde')]
    negras = [(num, 'negro') for num in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24]]
    rojas  = [(num, 'rojo' ) for num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23]]

    ruleta = verde + negras + rojas
    random.shuffle(ruleta)
    return ruleta

def color_numero(numero):
    if numero == 0:
        return 'verde'
    elif numero in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24]:
        return 'negro'
    elif numero in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23]:
        return 'rojo'

def ruleta():
    os.system('cls')
    ruleta = crear_ruleta()
    dinero = 200.0
    print("Bienvenido a Yosi Juego Ruleta")

    while True:
        print("Dinero actual: ", dinero)
        print("\n¿Qué deseas hacer? \n\t1)Girar \n\t2)Retirarte")
        opcion = input("Opción: ")

        if opcion == '1':
            while True:
                print(ruleta)
                try:
                    opcion_usuario = int(input("\nSelecciona un número del 0-24: "))
                    if 0 <= opcion_usuario <= 24:
                        break
                    else:
                        mensajes(3)
                except ValueError:
                    mensajes(3)

            while True:
                print("Selecciona tu apuesta. Mínimo: 20 - Máximo: 5000. Dinero disponible:", dinero)
                try:
                    apuesta = float(input("Apuesta: "))
                    if 20.0 <= apuesta <= dinero:
                        dinero -= apuesta
                        print("Girando la ruleta...")
                        time.sleep(3)

                        valor_azar = random.choice(ruleta) 
                        numero_ganador, color_ganador = valor_azar

                        print("\nNúmero ganador: ", numero_ganador, "Color: ", color_ganador)
                        
                        if opcion_usuario == numero_ganador:
                            if numero_ganador ==0:
                                ganancias = apuesta*10
                            else:
                                ganancias = apuesta * 4

                            dinero += ganancias
                            mensajes(1)

                        elif color_ganador == color_numero(opcion_usuario):
                            ganancias = apuesta * 2  
                            dinero += ganancias
                            mensajes(1)
                            
                        else:
                            mensajes(2)

                        break 

                    else:
                        mensajes(3)
                except ValueError:
                    mensajes(3)

        elif opcion == '2':
            print("Te has retirado, tu total de dinero es: ", dinero)
            limpiar_pantalla()
            break

        else:
            mensajes(3)

#Funciones juego blackjack
def crear_baraja():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(valor, palo) for palo in palos for valor in valores]
    random.shuffle(baraja)

    return baraja

def calcular_puntuacion(mano):
    valor_total = 0

    for carta in mano:
        valor = carta[0]

        if valor in ['J','Q','K']:
            valor_total += 10

        elif valor == 'A':
            valor_as = 0
            while valor_as!=1 or valor_as!=11:
                try:
                    print("Tienes un as, ¿cuál valor deseas darle?")
                    valor_as = int(input("Valor, 11 o 1: "))

                    if valor_as == 11 or valor_as ==1:
                        break
                    else:
                        print("Ingresa un valor de 11 o 1")
                        limpiar_pantalla()

                except ValueError:
                    mensajes(3)

            valor_total+=valor_as

        else:
            valor_total += int(valor)

    return valor_total

def mostrar_mano(mano):
    print("Tus cartas son: ")
    print(", ".join(f"{valor} de {palo}" for valor, palo in mano))

def blackjack():
    os.system('cls')
    validar_gane_jugador = True

    baraja = crear_baraja()
    mano_jugador = [baraja.pop(), baraja.pop()]
    print("Bienvenido al Yosi Juego BlackJack")

    valor_jugador = calcular_puntuacion(mano_jugador)

    while True:
        os.system('cls')
        mostrar_mano(mano_jugador)
        print("Tu puntuación es: ", valor_jugador)
        print("\n¿Qué deseas hacer? \n\t1)Pedir otra carta \n\t2)Quedarte")
        opcion = input("Opción: ")

        if opcion == '1':
            os.system('cls')
            if valor_jugador <= 21:
                mano_jugador.append(baraja.pop())
                mostrar_mano(mano_jugador)

                valor_jugador = calcular_puntuacion(mano_jugador)
                print("Tu puntuación es: ", valor_jugador)

                if valor_jugador > 21:
                    break

            else:
                validar_gane_jugador = False
                mensajes(2)
                break
        
        elif opcion=='2':
            break

        else:
            mensajes(3)
    
    valor_oponente = random.randint(15,21)
    
    if validar_gane_jugador:
        print("\nPuntos:",valor_jugador,"Puntos crupier:",valor_oponente)

        if valor_jugador == valor_oponente:
            print("Ha sido un empate")
            limpiar_pantalla()
        
        elif valor_jugador > valor_oponente and valor_jugador<=21:
            mensajes(1)

        else:
            mensajes(2)
#---------------------------------

if __name__ == "__main__":
    salir = False
    while True:

        if salir:
            print("Acabas de salir, vuelve pronto")
            limpiar_pantalla()
            break

        else:
            menu()
            salir = seleccionar_opcion_menu()
