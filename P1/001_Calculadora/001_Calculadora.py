#Samuel Josimar Orozco Torres -> 21110380 -> 6E2
import os
import time 
os.system('cls')

suma            = lambda a,b: a+b
resta           = lambda a,b: a-b
multiplicacion  = lambda a,b: a*b
exponente       = lambda a,b: pow(a,b)
raiz            = lambda a,b: pow(a,1/b)
division        = lambda a,b: a/b
division_entera = lambda a,b: a//b
modulo          = lambda a,b: a%b

def limpiar_pantalla():
    input("Presiona una tecla para continuar...")
    os.system('cls')

def mensaje_error(tipo):
    opc = str(tipo)

    if opc=='1':
        print("No puedes dividir por un número igual a cero")

    elif opc=='2':
        print("Ingresa un valor dentro del rango")
    
    elif opc=='3':
        print("Ingresa una opción válida")

    input("Presione cualquier tecla para continuar...")
    os.system('cls')

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

def opciones_menu():
    while True:
        try:
            opcion_menu = int(input("Opción: "))
            break
        except Exception:
            mensaje_error(3)

    if 0 < opcion_menu < 8:
        while True:
            try:
                if opcion_menu == 4 or opcion_menu == 6:
                    a = float(input("\tIngresa un número: "))
                    
                    if opcion_menu == 4: b = float(input("\tIngresa la potencia: "))
                    else:                b = float(input("\tIngresa la raíz: "))

                else:
                    a = float(input("\tIngresa el primer  número: "))
                    b = float(input("\tIngresa el segundo número: "))
                break
            except Exception:
                mensaje_error(2)

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

    elif opcion_menu == 0:
        return True
        
    else:
        mensaje_error(2)

    time.sleep(3)
    os.system('cls')
    return False

if __name__ == "__main__":
    salir = False
    while True:

        if salir:
            print("Acabas de salir, vuelve pronto")
            break

        else:
            menu()
            salir = opciones_menu()