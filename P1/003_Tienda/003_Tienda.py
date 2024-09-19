#Samuel Josimar Orozco Torres -> 21110380 -> 6E2
from colorama import Fore, Style
from datetime import datetime
from time import sleep
import os

#---CLASES---
class  General:
    def __init__(self,id,nombre):
        self.id     = id
        self.nombre = nombre

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
    
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

class User(General):    #HERENCIA DE LA CLASE <GENERAL>
    def __init__(self, id, nombre, edad, domicilio, saldo):
        super().__init__(id,nombre)     #LLAMA AL CONSTRUCTOR DE LA CLASE PADRE
        self.edad       = edad
        self.domcilio   = domicilio
        self.saldo      = saldo
    
    def get_edad(self):
        return self.edad
    
    def get_domicilio(self):
        return self.domcilio
    
    def get_saldo(self):
        return self.saldo
    
    def set_edad(self, edad):
        self.edad = edad

    def set_domicilio(self, domicilio):
        self.domcilio = domicilio

    def set_saldo(self, saldo):
        self.saldo = saldo

class Item(General):
    def __init__(self, id, nombre, precio, cantidad, proveedor):
        super().__init__(id,nombre)
        self.precio     = precio
        self.cantidad   = cantidad
        self.proveedor  = proveedor

    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.cantidad
    
    def get_proveedor(self):
        return self.proveedor
    
    def set_precio(self, precio):
        self.precio = precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_proveedor(self, proveedor):
        self.proveedor = proveedor
#---FIN CLASES---

#---FUNCIONES CONSOLA---
def limpiar_pantalla():
    input("Presiona cualquier tecla para continuar...")
    os.system('cls')

def mensajes(tipo):
    if tipo==0:
        borrar_mensaje_consola(Fore.RED+"Ingresa una opcion valida")
    elif tipo==1:
        borrar_mensaje_consola(Fore.CYAN+"El tipo de dato no es correcto")
    print(Style.RESET_ALL)

def borrar_mensaje_consola(mensaje):
    os.sys.stdout.write(mensaje)
    os.sys.stdout.flush()           #FUERZA LA ESCRITURA DEL MENSAJE POR CONSOLA
    sleep(3)
    os.sys.stdout.write('\r' + ' ' * len(mensaje) + '\r')
    os.sys.stdout.flush()
#---FIN FUNCIONES CONSOLA---

#---FUNCIONES BASICAS---
def agregar_usuario(lista_usuarios,bandera_editar):
    os.system('cls')
    if not bandera_editar: print("\tAgregar un nuevo usuario\n")

    id = len(lista_usuarios)+1
    nombre = input("Nombre          : ")
    nombre = nombre.title()

    while True:
        try:
            edad = int(input("Edad (15-80)    : "))
            if 15 < edad < 80:
                break
            else:
                mensajes(1)
        except Exception:
            mensajes(0)
    while True:
        try:
            saldo = float(input("Saldo (positivo): "))
            if 0 <= saldo:
                break
            else:
                mensajes(1)
        except Exception:
            mensajes(0)

    domicilio = input("Domicilio       : ")
    domicilio = domicilio.capitalize()
    usuario_nuevo = User(id, nombre, edad, domicilio, saldo)

    if not bandera_editar:
        lista_usuarios.append(usuario_nuevo)

        print("\tSe agregó el usuario ",nombre," correctamente\n")
        limpiar_pantalla()
        return lista_usuarios
    
    else:
        return usuario_nuevo

def agregar_articulo(lista_articulos,bandera_editar):
    os.system('cls')
    if not bandera_editar: print("\tAgregar un nuevo artículo\n")

    id = len(lista_articulos)+1
    nombre = input("Nombre             : ")
    nombre = nombre.title()

    while True:
        try:
            precio = float(input("Precio (positivo)  : "))
            if 0 < precio:
                break
            else:
                mensajes(1)
        except Exception:
            mensajes(0)
    while True:
        try:
            cantidad = int(input("Cantidad (positiva): "))
            if 0 < cantidad:
                break
            else:
                mensajes(1)
        except Exception:
            mensajes(0)

    proveedor = input("Proveedor          : ")
    proveedor.capitalize()
        
    articulo_nuevo = Item(id,nombre,precio,cantidad,proveedor)

    if not bandera_editar:
        lista_articulos.append(articulo_nuevo)

        print("\tSe agregó el artículo ",nombre," correctamente\n")
        limpiar_pantalla()
        return lista_articulos
    
    else:
        return articulo_nuevo

def editar_usuario(lista_usuarios):
    aux_indice_existente = False

    if not validar_arreglo_vacio(lista_usuarios):
        os.system('cls')
        print("\tEditar usuario\n")

        while True:
            try:
                mostrar_lista(lista_usuarios,0)
                indice = int(input("Ingresa el id para editar: "))
                if 0 <= indice <= len(lista_usuarios):
                    break
                else:
                    mensajes(1)
            except Exception:
                mensajes(0)

        for usuario in lista_usuarios:
            if usuario.get_id() == indice:
                aux_indice_existente = True
                break

        if aux_indice_existente:
            aux_objeto_usuario = agregar_usuario(lista_usuarios,True)
            lista_usuarios[indice-1].set_nombre(aux_objeto_usuario.get_nombre())   
            lista_usuarios[indice-1].set_edad(aux_objeto_usuario.get_edad())     
            lista_usuarios[indice-1].set_saldo(aux_objeto_usuario.get_saldo())    
            lista_usuarios[indice-1].set_domicilio(aux_objeto_usuario.get_domicilio())

            print("\tSe actualizó un usuario correctamente\n")
            limpiar_pantalla()
        else:
            mensajes(0)
            limpiar_pantalla()
    return lista_usuarios

def editar_articulo(lista_articulos):
    aux_indice_existente = False

    if not validar_arreglo_vacio(lista_articulos):
        os.system('cls')
        print("\tEditar artículo\n")

        while True:
            try:
                mostrar_lista(lista_articulos,1)
                indice = int(input("Ingresa el id para editar: "))
                if 0 <= indice <= len(lista_articulos):
                    break
                else:
                    mensajes(1)
            except Exception:
                mensajes(0)

        for articulo in lista_articulos:
            if articulo.get_id() == indice:
                aux_indice_existente = True
                break

        if aux_indice_existente:
            aux_objeto_articulo = agregar_articulo(lista_articulos,True)
            lista_articulos[indice-1].set_nombre(aux_objeto_articulo.get_nombre())
            lista_articulos[indice-1].set_precio(aux_objeto_articulo.get_precio())
            lista_articulos[indice-1].set_cantidad(aux_objeto_articulo.get_cantidad())
            lista_articulos[indice-1].set_proveedor(aux_objeto_articulo.get_proveedor())

            print("\tSe actualizó un artículo correctamente\n")
            limpiar_pantalla()

        else:
            os.system('cls')
            mensajes(0)
            limpiar_pantalla()
    return lista_articulos

def borrar_item(lista):
    aux_indice_existente = False

    if not validar_arreglo_vacio(lista):
        os.system('cls') 
        print("\tBorrar artículo")

        while True:
            try:
                indice = int(input("Ingresa el id para eliminar: "))
                break
            except Exception:
                mensajes(0)

        for item in lista:
            if item.get_id() == indice:
                aux_indice_existente = True
                break
        
        if aux_indice_existente:
            del lista[indice-1]
            aux_indice_nuevo = 1

            for item in lista:
                item.set_id(aux_indice_nuevo)
                aux_indice_nuevo += 1

            print("\tSe borró un registro correctamente\n")
            limpiar_pantalla()

        else:
            os.system('cls')
            mensajes(0)
            limpiar_pantalla()

    return lista

def mostrar_lista(lista,tipo):
    if not validar_arreglo_vacio(lista):
        os.system('cls')
        print("\tMostrando elementos\n")

        for item in lista:
            print("\tId:     ",item.get_id())
            print("\tNombre: ",item.get_nombre())

            if tipo == 0:
                print("\tEdad:      ",item.get_edad())
                print("\tDomicilio: ",item.get_domicilio())
                print("\tSaldo:     ",item.get_saldo(),"\n")
            elif tipo == 1:
                print("\tPrecio:    ",item.get_precio())
                print("\tCantidad:  ",item.get_cantidad())
                print("\tProveedor: ",item.get_proveedor(),"\n")

    limpiar_pantalla()
#---FIN FUNCIONES BASICAS---

#---FUNCIONES LISTAS---
def validar_arreglo_vacio(lista):
    if len(lista)==0:
        print("\tSin registros")
        limpiar_pantalla()
        return True
    
    return False

def opcion_comprar(lista_usuarios,lista_articulos):

    if not validar_arreglo_vacio(lista_articulos) and not validar_arreglo_vacio(lista_usuarios):
        aux_total_articulos = len(lista_articulos)
        aux_total_usuarios  = len(lista_usuarios)

        while True:
            try:
                mostrar_lista(lista_usuarios,0)
                indice_usuario_compra = int(input("\n\t Selecciona el id del usuario: "))
                indice_usuario_compra-=1
                if 0 <= indice_usuario_compra <= aux_total_usuarios:
                    break
                else:
                    mensajes(1)
            except Exception:
                mensajes(0)

        aux_nombre_usuario = lista_usuarios[indice_usuario_compra].get_nombre()
        aux_saldo_usuario  = lista_usuarios[indice_usuario_compra].get_saldo()
        aux_precio_total = 0 

        if aux_saldo_usuario > 0:
            aux_lista_total_cantidades = []
            aux_lista_total_precios    = []
            aux_lista_temporal_cantidades = []

            for articulo in lista_articulos:
                aux_lista_total_cantidades.append(articulo.get_cantidad())
                aux_lista_total_precios.append(articulo.get_precio())
                aux_lista_temporal_cantidades.append(0)

            aux_validar = False #Comprobar si existe algun articulo en el carrito
            while True:
                os.system('cls')
                print("\n\tBienvenido ",aux_nombre_usuario, " tu saldo es: ",aux_saldo_usuario)
                print("\n\tSelecciona una opción del menú")
                print("\t1. Comprar")
                print("\t2. Ver carrito: ")
                print("\t3. Pagar")
                print("\t4. Salir")
                opcion_submenu = input("\n\tSelecciona una opción: ")

                if opcion_submenu == '1':
                    while True:
                        try:
                            mostrar_lista(lista_articulos,1)
                            indice_articulo_compra = int(input("\tSelecciona el id del producto: "))
                            indice_articulo_compra-=1
                            if 0 <= indice_articulo_compra <= aux_total_articulos:
                                break
                            else:
                                mensajes(1)
                        except Exception:
                            mensajes(0)

                    while True:
                        try:
                            aux_cantidad_articulos_compra = int(input("\tSelecciona la cantidad del producto: "))
                            if aux_cantidad_articulos_compra > 0:
                                break
                            else:
                                mensajes(1)
                        except Exception:
                            mensajes(0)
                    
                    #VERIFICACIONES
                    if aux_cantidad_articulos_compra+aux_lista_temporal_cantidades[indice_articulo_compra]>aux_lista_total_cantidades[indice_articulo_compra]:
                        os.system('cls')
                        print("\tNo puedes ingresar un número mayor de produtos a los existentes\n")
                        limpiar_pantalla()

                    elif aux_precio_total + aux_lista_total_precios[indice_articulo_compra]*aux_cantidad_articulos_compra > aux_saldo_usuario:
                        os.system('cls')
                        print("\tSaldo insuficiente\n")
                        limpiar_pantalla()

                    else:
                        aux_lista_temporal_cantidades[indice_articulo_compra] += aux_cantidad_articulos_compra
                        aux_precio_total += aux_lista_total_precios[indice_articulo_compra]*aux_cantidad_articulos_compra
                        print("\n\tSe han añadido un producto a tu carrito")
                        aux_validar = True
                        limpiar_pantalla()

                elif opcion_submenu == '2':
                    if aux_validar:
                        aux_suma_total_precios = 0

                        for indice in range(aux_total_articulos):
                            if aux_lista_temporal_cantidades[indice] > 0:
                                print("\tNombre  : ",lista_articulos[indice].get_nombre())
                                print("\tCantidad: ",aux_lista_temporal_cantidades[indice])
                                print("\tPrecio  : ",aux_lista_total_precios[indice]*aux_lista_temporal_cantidades[indice],"\n")
                                aux_suma_total_precios += aux_lista_total_precios[indice]*aux_lista_temporal_cantidades[indice]

                        print("\tTotal a pagar: ",aux_suma_total_precios)
                    else:
                        print("\tTu carrito esta vacio: ")
                    limpiar_pantalla()

                elif opcion_submenu == '3':
                    if aux_validar:
                        if aux_saldo_usuario - aux_precio_total < 0:
                            print("\tNo hay dinero suficiente\n")
                            limpiar_pantalla()
                        else:
                            lista_usuarios[indice_usuario_compra].set_saldo(aux_saldo_usuario-aux_precio_total)
                            aux_indice_asigar = 0

                            aux_lista_ticket = []
                            aux_tupla_ticket = ()

                            for articulo in lista_articulos:
                                articulo.set_cantidad(aux_lista_total_cantidades[aux_indice_asigar]  - aux_lista_temporal_cantidades[aux_indice_asigar])
                                
                                if aux_lista_temporal_cantidades[aux_indice_asigar] > 0:
                                    aux_nombre_articulo   = lista_articulos[aux_indice_asigar].get_nombre()
                                    aux_cantidad_articulo = aux_lista_temporal_cantidades[aux_indice_asigar]
                                    aux_precio_articulo   = aux_lista_total_precios[aux_indice_asigar]*aux_lista_temporal_cantidades[aux_indice_asigar]

                                    aux_tupla_ticket = (aux_nombre_articulo,aux_cantidad_articulo,aux_precio_articulo)
                                    aux_lista_ticket.append(aux_tupla_ticket)

                                aux_indice_asigar +=1
                            
                            print("\n\tSe ha realizado la compra correctamente")
                            generar_ticket(aux_nombre_usuario,aux_lista_ticket)
                            print("Volviendo al menu principal...")
                            sleep(3)
                            os.system('cls')
                            break

                    else:
                        ("No tienes articulos guardados")
                        limpiar_pantalla()

                elif opcion_submenu == '4':
                    print("Volviendo al menu principal...")
                    sleep(3)
                    break
                else:
                    mensajes(1)
        else:
            print("Saldo insuficiente")
            limpiar_pantalla()
#---FIN FUNCIONES LISTAS---

#---FUNCIONES IMPRESION DE DATOS EXTERNOS---
def generar_ticket(usuario,lista_compra):
    hora_actual  = datetime.now()
    mensaje = usuario+"Ticket.txt"

    with open(mensaje,'w') as archivo:  #ASEGURAR QUE EL ARCHIVO SE CIERRE DE FORMA CORRECTA
        archivo.write("\tYosiCompro\n")
        archivo.write(f"Fecha:{hora_actual}\n")

        for articulo in lista_compra:
            archivo.write("Nombre:   "+articulo[0]+"\n")
            archivo.write("Cantidad: "+str(articulo[1])+"\n")
            archivo.write("Precio:   "+str(articulo[2])+"\n")

def cargar_datos(lista_usuarios,lista_articulos):
    with open('Datos.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(", ")
            #STRIP(): ELIMINA LOS CARACTERES INNECESARIOS AL PRINCIPIO Y FINAL DE LA LINEA
            #SPLIT(): DIVIDE LA LÍNEA EN UNA LISTA, UTILIZANDO ", " COMO DELIMITADOR

            clase = datos[0]

            if clase == "User":
                id          = int(datos[1])
                nombre      = datos[2]
                edad        = int(datos[3])
                domicilio   = datos[4]
                saldo       = float(datos[5])

                usuario = User(id,nombre,edad,domicilio,saldo)
                lista_usuarios.append(usuario)
            
            elif clase == "Item":
                id          = int(datos[1])
                nombre      = datos[2]
                precio      = float(datos[3])
                cantidad    = int(datos[4])
                proveedor   = datos[5]

                item = Item(id,nombre,precio,cantidad,proveedor)
                lista_articulos.append(item)

    return lista_usuarios,lista_articulos
#---FIN FUNCIONES IMPRESION DE DATOS EXTERNOS---

#---FUNCIONES MENU---
def menu():
    print("\n\tBienvenido selecciona una opción:")
    print("\t1. Agregar  Usuario")
    print("\t2. Agregar  Artículo")
    print("\t3. Editar   Usuario")
    print("\t4. Editar   Artículo")
    print("\t5. Borrar   Usuario")
    print("\t6. Borrar   Artículo")
    print("\t7. Mostrar  Usuarios")
    print("\t8. Mostrar  Artículos")
    print("\t9. Realizar compra")
    print("\t0. Salir")

def seleccionar_opcion_menu(lista_usuarios, lista_articulos):
    opcion = input("\n\tSelecciona una opción dentro del rango: ")

    if opcion == '1':
        lista_usuarios = agregar_usuario(lista_usuarios,False)

    elif opcion == '2':
        lista_articulos = agregar_articulo(lista_articulos,False)

    elif opcion == '3':
        lista_usuarios = editar_usuario(lista_usuarios)

    elif opcion == '4':
        lista_articulos = editar_articulo(lista_articulos)

    elif opcion == '5':
        lista_usuarios = borrar_item(lista_usuarios)

    elif opcion == '6':
        lista_articulos = borrar_item(lista_articulos)

    elif opcion == '7':
        mostrar_lista(lista_usuarios,0)

    elif opcion == '8':
        mostrar_lista(lista_articulos,1)

    elif opcion == '9':
        opcion_comprar(lista_usuarios,lista_articulos)

    elif opcion == '0':
        print("Saliendo del programa...")
        return True
        
    else:
        print("Selecciona una opción dentro del rango de valores")
        limpiar_pantalla()

    return False
#---FIN FUNCIONES MENU---

if __name__ == "__main__":
    salir = False
    lista_usuarios =  []
    lista_articulos = []

    #CARGAR DATOS
    lista_usuarios, lista_articulos = cargar_datos(lista_usuarios,lista_articulos)
    
    while True:

        if salir:
            print("Acabas de salir, vuelve pronto")
            limpiar_pantalla()
            break

        else:
            menu()
            salir = seleccionar_opcion_menu(lista_usuarios,lista_articulos)