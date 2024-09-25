#Samuel Josimar Orozco Torres -> 21110380 -> 6E2
import os   # Importa el módulo os, que permite interactuar con el sistema operativo, por ejemplo, para limpiar la pantalla.
import time # Importa el módulo time para poder usar funciones relacionadas con el tiempo, como sleep.

os.system('cls') # Limpia la consola al inicio del programa.

# Se definen funciones usando lambdas para realizar operaciones matemáticas básicas 
# como suma, resta, multiplicación, exponente, raíz, división, división entera y módulo.
suma            = lambda a,b: a+b
resta           = lambda a,b: a-b
multiplicacion  = lambda a,b: a*b
exponente       = lambda a,b: pow(a,b)
raiz            = lambda a,b: pow(a,1/b)
division        = lambda a,b: a/b
division_entera = lambda a,b: a//b
modulo          = lambda a,b: a%b
#--------------------------------------------------------------------

#Definimos una función con la palabra reservada def seguido del nombre de la función y los parámetros si llegase a tener.
# Su función es esperar que el usuario presione una tecla y luego limpia la pantalla con os.system('cls')
def limpiar_pantalla():
    input("Presiona una tecla para continuar...")
    os.system('cls')
#--------------------------------------------------------------------

# Función que recibe un tipo de error (número) y muestra un mensaje correspondiente.
def mensaje_error(tipo):
    opc = str(tipo)

    if opc=='1':
        print("No puedes dividir por un número igual a cero")

    elif opc=='2':
        print("Ingresa un valor dentro del rango")
    
    elif opc=='3':
        print("Ingresa una opción válida")

    limpiar_pantalla()
#----------------------------------------------------------------

# Muestra las opciones disponibles para el usuario.
def menu():
    print("\n\tBienvenido a YosiCalculo selecciona una opción:")
    print("\t1. Sumar")
    print("\t2. Restar")
    print("\t3. Multiplicar")
    print("\t4. Exponente")
    print("\t5. División")
    print("\t6. Raíz")
    print("\t7. Módulo")
    print("\t0. Salir")
#----------------------------------------------------------------

# Captura la opción del menú que el usuario introduce. Si no es un número válido, llama a mensaje_error para mostrar un error.
def opciones_menu():
    while True:
        try:
            opcion_menu = int(input("Opción: "))
            break
        except Exception:
            mensaje_error(3)
# ---------------------------------------------------------------

# Si la opción está dentro del rango válido (entre 1 y 7), pide al usuario que ingrese los números correspondientes. 
# En los casos de exponente o raíz, maneja los valores de forma particular.
    if 0 < opcion_menu < 8:
        while True:
            try:
                if opcion_menu == 4 or opcion_menu == 6:
                    a = float(input("\tIngresa un número: "))
                    
                    if opcion_menu == 4: b = float(input("\tIngresa la potencia: "))
                    else:                b = float(input("\tIngresa la raíz: "))
# ------------------------------------------------------------------------------------

# Para las demás opciones, solicita dos números, y si se introduce algo no válido, llama a mensaje_error(2)
                else:
                    a = float(input("\tIngresa el primer  número: "))
                    b = float(input("\tIngresa el segundo número: "))
                break
            except Exception:
                mensaje_error(2)
# ------------------------------------------------------------------------

# Dependiendo de la opción seleccionada por el usuario, accede a la función establecida en cada caso.
# Realizando la operación correspondiente.
    if opcion_menu == 1:
        print("El resultado es:",suma(a,b))

    elif opcion_menu == 2:
        print("El resultado es:",resta(a,b))

    elif opcion_menu == 3:
        print("El resultado es: ",round(multiplicacion(a,b),3))

    elif opcion_menu == 4:
        print("El resultado es: ",round(exponente(a,b),3))

    elif opcion_menu == 5:
        if b!=0:
            print("División: ")
            print("El resultado es: ",round(division(a,b),3))
            print("División entera: ",division_entera(a,b))

        else:
            mensaje_error(1)
        
    elif opcion_menu == 6:
        print("El resultado es: ",round(raiz(a,b),3))

    elif opcion_menu == 7:
        print("El módulo es: ",modulo(a,b))
# -----------------------------------------------------------------------

# Si el usuario selecciona la opción cero (0) salimos del programa
    elif opcion_menu == 0:
        return True
# -----------------------------------------------------------------------
    else:
        mensaje_error(2)

    time.sleep(3)
    os.system('cls')
    return False

# Este bloque principal ejecuta el ciclo del programa. 
# Si salir es True, muestra un mensaje de despedida y termina. Si no, llama al menú y ejecuta la función opciones_menu.
if __name__ == "__main__":
    salir = False
    while True:

        if salir:
            print("Acabas de salir, vuelve pronto")
            break

        else:
            menu()
            salir = opciones_menu()
# ---------------------------------------------------------