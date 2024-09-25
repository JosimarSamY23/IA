#Samuel Josimar Orozco Torres -> 21110380 -> 6E2
import os       #Importamos el módulo para poder realizar comandos en la consola del sistema
import random   #Importamos el módulo para generar valores aleatorios
import time     #Importamos el módulo para hacer pausas de tiempo en la consola del sistema

os.system('cls') #Limpiamos la pantalla

#Funciones
#Función def menu() -> Muestra las diferentes opciones por pantalla
def menu():
    print("\n\tBienvenido a YosiJuego selecciona una opción:")
    print("\t1. Adivina el número")
    print("\t2. Tres en raya")
    print("\t3. Deal or no deal")
    print("\t4. Simon dice")
    print("\t5. Ruleta")
    print("\t6. Veintiuno")
    print("\t0. Salir")
# -------------------------------------------------------------

# Captura la opción del menú que el usuario introduce. 
# Si no es un número válido, llama a mensaje_error para mostrar un error.
# Además de realizar la función correspondiente a la opción del usuario.
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
# --------------------------------------------------------------------

# Función que recibe un tipo de error (número) y muestra un mensaje correspondiente.
def mensajes(tipo):
    if tipo == 1:
        print("Felicidades has ganado")
    elif tipo == 2:
        print("Lo siento has perdido")
    else:
        print("Ingresa una opción válida")
    
    limpiar_pantalla()
# -------------------------------------------------------------------
    
# Espera que el usuario presione una tecla y luego limpia la pantalla con os.system('cls').
def limpiar_pantalla():
    input("Presione una tecla para continuar")
    os.system('cls')
# ---------------------------------------------------

# Funciones juego adivina el numero #
def adivina_numero():
    os.system('cls')
    num = random.randint(1,100) # El sistema elige un número aleatorio entre 1-100.
    num_usuario = 0             # Se almacena aquí el número ingresado por el usuario.
    contador    = 1

    lista_num_ingresados = []   # Se almacenarán aquí los números ingresados por el usuario.

    while True:
        # Se válida que se ingrese una opción dentro del rango de números
        try:
            if contador!=8:
                print("Encuentra el número de 1 - 100. Intento:",contador,"/ 7")
                if 0 < len(lista_num_ingresados):
                    print("Numeros ingresados: ",lista_num_ingresados) # Se muestran los números ingresados anteriormente.

                num_usuario = int(input("Elige un número: "))
                if num_usuario == num: # Se válida que el número sea igual.
                    mensajes(1)
                    return              # Utilizamos return para salir de la función.
                elif num_usuario > num: # Se válida que el número es mayor.
                    print("El número es menor")
                else:                   # Se válida que el número es menor.
                    print("El número es mayor")
            else:
                mensajes(2)
                print("El número era: ", str(num)) # Si se pierde, se muestra el número elegido por el sistema.
                time.sleep(3)
                os.system('cls')
                return

            contador+=1
            lista_num_ingresados.append(num_usuario) # Se almacena el número ingresado por el usuario.
            limpiar_pantalla()

        except ValueError: 
            mensajes(3)
#---------------------------------

#Funciones juego tres en raya
def crear_tablero():
    tablero = [[" " for _ in range(3)] for _ in range(3)] # Se crea una matriz de [3][3] con valor en blanco " ".
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:        
        print("|".join(fila)) # Se concatena el símbolo | para cada casilla del tablero, lo cuál hará la divisiín de las filas.
        print("-"*6)          # Se imprime el símbolo - para dividir cada columna del tablero.

def verificar_ganador(tablero,turno):
    jugadores = ["X","O"]
    jugador = ""

    if turno:   # Verificamos el turno del jugador.
        jugador = jugadores[0]
    else:
        jugador = jugadores[1]

    for i in range(3):
        #VERIFICA TODOS LOS ELEMENTOS DE LA FILA.                #VERIFICA TODOS LOS ELEMENTOS DE LA COLUMNA.
        if all([tablero[i][j] == jugador for j in range(3)]) or all([tablero[j][i] == jugador for j in range(3)]):
            return True
        # Verifica las diagonales del tablero.
        if(tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador) or (tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador):
            return True # Retorna True si un jugador tiene tres elementos.
        
        return False
    
def tablero_lleno(tablero):
    # Verificamos que el tablero en todas sus casillas esté ocupado por algún jugador.
    if all([celda!= " " for fila in tablero for celda in fila]):
        return True
    
    return False

def posicion_numero(numero):
    # Número es un rango de valor de 1-9 que serían las casillas reales del tablero
    # Dependiendo del número es el valor fila, columna, que le corresponde en el tablero.
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
    # Aquí tenemos la lógica del juego del gato.
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
                print("Turno Jugador"+str(jugador_actual+1)) #Imprimimos el turno del jugador correspondiente.
                imprimir_tablero(tablero)   # Mostramos el tablero por pantalla.
                opc_jugador = int(input("Elige la posicion del 1-9: "))
                fila,columna = posicion_numero(opc_jugador) # Agignamos valor de fila,columna dependiendo la posición dentro del tablero.

                if tablero[fila][columna] == " ": # Válidamos que la posición no esté ocupada.
                    tablero[fila][columna] = jugadores[jugador_actual] # Asignamos al tablero el símbolo del jugador.
                    break
                
                else:
                    print("La posición ya esta ocupada")
                    limpiar_pantalla()

            except (ValueError, IndexError, TypeError):
                mensajes(3)

        if verificar_ganador(tablero,turno):    # Válidamos que algún jugador haya ganado.
            if turno: print("Ha ganado el jugador 1")
            else: print("Ha ganado el jugador 2")
            limpiar_pantalla()
            break

        if tablero_lleno(tablero):  # Válidamos que el tablero esté lleno.
            print("Es un empate")
            limpiar_pantalla()
            break

        turno = not turno           # Cambiamos el turno del jugdor.
#---------------------------------

#Funiones juego deal or no deal
def deal():
    os.system('cls')
    valores_bajos = [1,5,10,50,100,250,500,750]
    valores_altos = [1000,2500,5000,10000,25000,50000,75000,100000]
    valores_maletines = valores_bajos + valores_altos # Realizamos una nueva lista concatenando los valores de dos listas.
    random.shuffle(valores_maletines) # Reordenamos los valores dentro de la lista en forma aleatoria.

    maletin_usuario = [] # Se almacena el índice y el valor del elemento elegido por el usuario.
    
    rondas = [4,3,3,2,1,1] # La cantidad de maletines que pueden ser abiertos por ronda.
    ronda = 0   # Contador de rondas.
    lista_maletines_index = [(indice+1, valor) for indice, valor in enumerate(valores_maletines)]
    # Instrucción que asigna de forma ordenada del 1-16 el valor que contiene la lista.
    # (1, valor) es una tupla que contiene un índice ordenado y un valor reordenado anteriormente.

    while True:
        print("\nMaletines")
        mostrar_valores(lista_maletines_index) #Mosramos los maletines existentes
        print("\nEsccoge tu maletin. \n1)Eleccion \n2)Aleatorio")
        opcion = input("Opcion: ")

        # El usuario selecciona su maletin por su cuenta o de forma aleatoria.
        # Aquí se válida que ingrese una opción correcta dentro de los rangos establecidos.
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
            maletin_usuario = random.choice(lista_maletines_index) # Se elige un maletin de forma aleatoria.
            break

        else:
            mensajes(3)
            continue
        break
        # -------------------------------------------------------------------------------------------
    
    # Se almacena el índice del maletin y su valor en variables independientes.
    indice_usuario, valor_usuario = maletin_usuario
    del lista_maletines_index[indice_usuario-1] # Se elimina el maletin del usuario de la lista de maletines.
    limpiar_pantalla()

    print("Tu maletín es el número ",indice_usuario,"con un valor oculto.")

#Inicio del juego aquí.
    aux = 0
    while True:
        validar_juego = True

        # En cada ronda, se abre una cierta cantidad de maletines.
        for maletines in rondas:
            for maletin in range(maletines):
                while True:
                    print("Ronda: ",str(ronda+1))
                    print("\nMaletines disponibles: ")

                    # Se muestran los maletines disponibles.
                    mostrar_valores(lista_maletines_index)

                    # Se muestran los valores altos y bajos.
                    print("\n\tValores bajos: ",valores_bajos)
                    print("\tValores altos: ",valores_altos)

                    # Se especifica cuántos maletines se avren por ronda y la cantidad de ellos abiertos actualmente.
                    print("\nMaletines por abrir: ",maletines)
                    print("Selecciona un maletin: ",str(maletin+1)," / ", str(maletines))

                    # Se válida que se ingrese un número de maletin dentro del rango 1-16
                    # Además de validar que no se puede ingresar un número de maletin ya elegido anteriormente.
                    try:
                        numero_maletin = int(input("\tNumero de maletin: "))

                        if 1 <= numero_maletin <= 16:
                            contador = 0
                            for x in lista_maletines_index:
                                if x[0] == numero_maletin: #Entramos al valor del maletin
                                    break
                                contador+=1

                            indice, valor = lista_maletines_index[contador]
                            # Se elimina el maletin elegido por el usuario.
                            del lista_maletines_index[contador]

                            # Se muestra el valor del maletin al usuario.
                            print("El maletin: ",indice," tiene el valor de: ",valor)

                            # Se elimina el valor de la lista de numeros altos o bajos.
                            valores_bajos, valores_altos = eliminar_valor(valores_bajos, valores_altos,valor)
                            limpiar_pantalla()
                            break
                        else:
                            mensajes(3)
                        
                    except (ValueError, IndexError):
                        mensajes(3)
                    # -----------------------------------------------------------------------------------
                aux +=1
                # Se comprueba que el número de maletines abiertos corresponda al número de maletines por ronda.
                if aux == rondas[ronda]:
                    print("\n\tValores bajos: ",valores_bajos)
                    print("\tValores altos: ",valores_altos)

                    # Se realiza la función de llamada al banco para regresar un valor.
                    cifra_banco = llamada_banco(valores_bajos, valores_altos, valor_usuario)
                    print("\nEl banco hará una oferta...")
                    time.sleep(5)

                    #Se muestra la cantidad de dinero ofrecida por el banco.
                    print("El banco ofrece la cantidad de: ",cifra_banco)

                    # Válida que el usuariom siga en el juego o se retire con el dinero ofrecido por el banco.
                    while True:
                        opc_banco = input("Aceptas la oferta s/n: ")

                        if opc_banco == 's' or opc_banco == 'S' or opc_banco == 'n' or opc_banco == 'N':
                            break
                        else:
                            mensajes(3)
                        
                    if opc_banco == 's':
                        os.system('cls')
                        print("Felicidades, has ganado: ",cifra_banco)
                        print("Tu maletin tenía la cantidad de: ",valor_usuario)
                        limpiar_pantalla()
                        validar_juego = False
                        break

                    elif opc_banco == 'n':
                        print("Sigues en el juego")
                        limpiar_pantalla()

                    ronda+=1
                    aux = 0

                    if ronda==6:
                        break
                    # ------------------------------------------------------------------------

            if not validar_juego:
                break

            if ronda==6:
                break
        
        if not validar_juego:
            break

        #Al llegar a la ultima instancia
        print("\n\tValores bajos: ",valores_bajos)
        print("\tValores altos: ",valores_altos)

        # Válida que el usuario se quede con su maletin o lo cambie por el último maletin.
        print("¿Deseas quedarte con tu maletin?\n1)Si, quedarme con el.\n2)No, cambiar maletin")
        opc_ultima = input("\tOpcion: ")

        # Se muestra el valor del maletin del usuario y del maletin restante.
        if opc_ultima == '1':
            print("Tu maletin <"+str(indice_usuario)+"> tiene la cantidad de: "+str(valor_usuario))
            mensajes(1)
            indice_usuario,valor_usuario = lista_maletines_index[0] # índice 0 porque es el único elemento restante de la lista.
            print("En el maletin <"+str(indice_usuario)+"> habia la cantidad de: "+str(valor_usuario))
            limpiar_pantalla()
            break

        elif opc_ultima == '2':
            print("Tu maletin <"+str(indice_usuario)+"> tiene la cantidad de: "+str(valor_usuario))
            indice_usuario,valor_usuario = lista_maletines_index[0]
            print("En el maletin <"+str(indice_usuario)+"> has ganado la cantidad de: "+str(valor_usuario))
            limpiar_pantalla()
            break
        # ----------------------------------------------------------------------------------------------------
        else:
            mensajes(3)
        # ------------------------------------------------------------------------------------------

def eliminar_valor(lista1,lista2,valor):
    # Se recorren las listas de valores bajos y altos para eliminar un valor determinado.
    # Una vez encontrado el valor lo elimina de la lista.
    a1 = lista1
    b1 = lista2

    if valor in lista1:
        a1.remove(valor)
        

    if valor in lista2:
        b1.remove(valor)

    return a1,b1

def llamada_banco(bajos, altos, valor_usuario):
    # Se realiza un promedio de los valores de los maletines restantes para llegar a una determinada cifra.
    # Esta parte fue consultada en chatGPT para que me diera una operación matemática.
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
    
    return promedio_total

def mostrar_valores(lista):
    # Muestra solamente el índice de los maletines sin mostrar el valor.
    maletines_disponibles = [tupla[0] for tupla in lista] # [0] contiene el índice -> (índice,valor)
    print(maletines_disponibles)
#---------------------------------

#Funiones juego simon dice
def mostrar_secuencia(secuencia):
    # Muestra la secuencia de números por pantalla.
    for numero in secuencia:
        # Flush = True. Funciona para mostrar en pantalla en la misma línea, es decir, da una pequeña
        # pausa y sigue mostrando los valores.
        print(numero, end=' <-> ', flush=True)
        time.sleep(2)
    
    os.system('cls')

def simon_dice():
    os.system('cls')
    print("¡Bienvenido a Yosi Dice!")
    secuencia = [] # Aquí se almacena la secuencia de números.
    ronda = 1      # El número de rondas

    while True:
        nuevo_numero = random.randint(1, 5) # Se elige un número aleatorio entre 1-5
        secuencia.append(nuevo_numero)      # Se agrega ese número a la secuencia.

        print("Ronda: ",ronda)          # Muestra la ronda actual de la partida.
        mostrar_secuencia(secuencia)    # Se muestra la secuencia de números.

        for i in range(ronda):
            while True:
                # Se válida que el número del usuario sea correcto al número de cada ronda.
                try:
                    print("¿Cual era el número "+str(i+1)+" ?")         
                    respuesta_usuario = int(input("Repite el número: "))    # El usuario ingresa el número
                    if respuesta_usuario == secuencia[i]:   # Válida que la respuesta del usuario sea igual al número de la secuencia
                        print("Correcto!")
                        break
                    else:
                        print("Incorrecto")
                        mensajes(2)
                        return              # Si se equivoca, sale de la función y se termina el juego.
                    
                except ValueError:
                    mensajes(3)
                # ---------------------------------------------------------------------------

        ronda += 1  # Aumenta la ronda al contestar correctamente.
#---------------------------------

#Funiones juego ruleta
def crear_ruleta():
    # Asignamos el valor y el color a cada casilla. El resultado es una lista de tuplas (número,color).
    verde  = [(0,   'verde')]
    negras = [(num, 'negro') for num in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24]]
    rojas  = [(num, 'rojo' ) for num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23]]

    # Realizamos una sola lista con la suma de todos los valores de las demás listas.
    ruleta = verde + negras + rojas
    random.shuffle(ruleta)
    return ruleta

def color_numero(numero):
    # Pasamos por parámetro el número seleccionado para obtener su color como valor.
    # Retornamos dicho valor.
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

    # Válida la opción del usuario.
    # Se debe selaccionar una opción válida del menú.
    while True:
        print("Dinero actual: ", dinero)
        print("\n¿Qué deseas hacer? \n\t1)Girar \n\t2)Retirarte")
        opcion = input("Opción: ")

        # Válida que el número este dentro del rango de valores 1-24.
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
        # ------------------------------------------------------

        # Válida que el monto ingresado no sea mayor al dinero del usuario.
            while True:
                print("Selecciona tu apuesta. Mínimo: 20 - Máximo: 5000. Dinero disponible:", dinero)
                try:
                    apuesta = float(input("Apuesta: "))
                    if 20.0 <= apuesta <= dinero:
                        # Se realiza la apuesta y se gira la ruleta.
                        dinero -= apuesta   # Se hace el descuento de la apuesta al dinero del usuario.
                        print("Girando la ruleta...")
                        time.sleep(3)
                        # Se selecciona un número al azar
                        valor_azar = random.choice(ruleta) 
                        # Se obtiene el número y el color ganador
                        numero_ganador, color_ganador = valor_azar

                        print("\nNúmero ganador: ", numero_ganador, "Color: ", color_ganador)
                        
                        # Se válida si el número es igual al número ganador
                        if opcion_usuario == numero_ganador:
                            if numero_ganador ==0:
                                ganancias = apuesta*10
                            else:
                                ganancias = apuesta * 4

                            dinero += ganancias
                            mensajes(1)

                        # Se válida si el color es igual al color ganador
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

        # Se válida la salida del usuario del juego
        elif opcion == '2':
            print("Te has retirado, tu total de dinero es: ", dinero)
            limpiar_pantalla()
            break
        else:
            mensajes(3)

#Funciones juego blackjack
def crear_baraja():
    # Se crea la baraja con los diferentes valores y símbolos correspondientes.
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(valor, palo) for palo in palos for valor in valores]

    # Se reordenan los valores dentro de la baraja (lista).
    random.shuffle(baraja)
    return baraja

def calcular_puntuacion(mano):
    valor_total = 0

    for carta in mano:
        valor = carta[0]

        # Se válida si la carta tiene una letra para darle el valor de 10.
        if valor in ['J','Q','K']:
            valor_total += 10 # Se hace la suma de puntos.

        # Se válida si la carta es un A para preguntarle al usuario que valor darle.
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
        # -----------------------------------------------------------------
            # Se hace la suma de puntos del A
            valor_total+=valor_as
        else:
            valor_total += int(valor)
    return valor_total

def mostrar_mano(mano):
    # Se muestran las cartas del usuario, mostrando su valor y símbolo.
    print("Tus cartas son: ")
    print(", ".join(f"{valor} de {palo}" for valor, palo in mano))
    # --------------------------------------------------------------

def blackjack():
    os.system('cls')
    validar_gane_jugador = True

    baraja = crear_baraja()
    # Se eliminan las cartas del jugador del mazo.
    mano_jugador = [baraja.pop(), baraja.pop()]
    print("Bienvenido al Yosi Juego BlackJack")

    # Se cálculan los puntos del usuario.
    valor_jugador = calcular_puntuacion(mano_jugador)

    while True:
        os.system('cls')
        # Se muestran las cartas del usuario.
        mostrar_mano(mano_jugador)
        print("Tu puntuación es: ", valor_jugador)
        # Se válida la opción del usuario de pedir otra carta o plantarse con sus puntos.
        print("\n¿Qué deseas hacer? \n\t1)Pedir otra carta \n\t2)Quedarte")
        opcion = input("Opción: ")

        if opcion == '1':
            os.system('cls')
            if valor_jugador <= 21: # Se da carta únicamente si el valor de puntos del usuario es menor a 21.
                mano_jugador.append(baraja.pop()) # Se elimina una carta y se añade a la mano del usuario.
                mostrar_mano(mano_jugador)  # Se muestran las cartas del usuario.

                # Se vuelve a calcular los puntos del usuario.
                valor_jugador = calcular_puntuacion(mano_jugador)
                print("Tu puntuación es: ", valor_jugador)

                # Si el valor es mayor sale del bucle.
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
    # -----------------------------------------------------------------
    # Se elige un valor aleatorio entre 15-21 para el crupier.
    valor_oponente = random.randint(15,21)
    
    # Se válida quien tiene el mayor puntaje entre el usuario y el crupier.
    if validar_gane_jugador:
        print("\nPuntos:",valor_jugador,"Puntos crupier:",valor_oponente)

        if valor_jugador == valor_oponente:
            print("Ha sido un empate")
            limpiar_pantalla()
        
        elif valor_jugador > valor_oponente and valor_jugador<=21:
            mensajes(1)

        else:
            mensajes(2)
    # ----------------------------------------------------------------------
#---------------------------------

# Este bloque principal ejecuta el ciclo del programa. 
# Si salir es True, muestra un mensaje de despedida y termina. Si no, llama al menú y ejecuta la función opciones_menu.
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
# ----------------------------------------------------------------
