#Samuel Josimar Orozco Torres -> 21110380 -> 6E2
from colorama import Fore, Style    #Importamos el módulo para cambiar el color del texto de la consola del sistema
from datetime import datetime       #Importamos el módulo para guardar la fecha actual
from time import sleep              #Importamos el módulo para darle una pausa a la consola.
import os                           #Importamos el módulo para trabajar en la consola del sistema.

#---CLASES---
# Definimos nuestras clases con sus atributos y métodos.
# Se utiliza la palabra reservada class seguido del nombre de la clase.
class  General:
    def __init__(self,id,nombre): # Con def __init__ inicializamos el constructor de la clase.
        self.id     = id          # Con la palabra reservada self, le indicamos que estamos trabajando con sus propios atributos y métodos.
        self.nombre = nombre

# Definimos los métodos get y set para trabajar de forma más práctica con los atributos de la clase.
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre
    
    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre
# --------------------------------------------------------------------------------

# La clase User, es para crear un objeto de una persona.
class User(General):    #HERENCIA DE LA CLASE <GENERAL>
    def __init__(self, id, nombre, edad, domicilio, saldo): # DEFINIMOS EL CONSTRUCTOR DE LA CLASE.
        super().__init__(id,nombre)     #LLAMA AL CONSTRUCTOR DE LA CLASE PADRE CON LA PALABRA RESERVADA SUPER
        self.edad       = edad
        self.domcilio   = domicilio
        self.saldo      = saldo
    
    # Definimos los métodos get y set para trabajar con sus atributos.
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
    # ----------------------------------------------------------------

# La clase Item, es para crear un objeto de un artículo. 
class Item(General):    # HERENCIA DE LA CLASE PADRE <GENERAL>
    def __init__(self, id, nombre, precio, cantidad, proveedor): # DEFINIMOS EL CONSTRUCTOR DE LA CLASE.
        super().__init__(id,nombre) # LLAMA AL CONSTRUCTOR DE LA CLASE PADRE CON LA PALABRA RESERVADA SUPER
        self.precio     = precio
        self.cantidad   = cantidad
        self.proveedor  = proveedor

    # Definimos los métodos get y set para trabajar con sus atributos.
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
def limpiar_pantalla(): # Se espera a que el usuario presione cualquier tecla para despues limpiar la consola.
    input("Presiona cualquier tecla para continuar...")
    os.system('cls')

def mensajes(tipo):
    # Se muestra un mensaje por pantalla mediante un parámetro llamado tipo.
    # Los mensajes se muestran de colores.
    if tipo==0:
        borrar_mensaje_consola(Fore.RED+"Ingresa una opcion valida") # Muestra el texto de color ROJO.
    elif tipo==1:
        borrar_mensaje_consola(Fore.CYAN+"El tipo de dato no es correcto") # Muestra el texto de color CYAN.
    print(Style.RESET_ALL) # Reestablece el color del texto, BLANCO.

def borrar_mensaje_consola(mensaje):
    os.sys.stdout.write(mensaje)    #Se muestra el mensaje por consola. Es otra manera de hacerlo, como la función print()
    os.sys.stdout.flush()           #FUERZA LA ESCRITURA DEL MENSAJE POR CONSOLA
    sleep(3)
    # Se posiciona al inicio de una línea y asigna el valor de " " a una cadena de texto, es decir borra el contenido de una cadena de texto.
    # Para al final posicionarse nuevamente al inicio.
    os.sys.stdout.write('\r' + ' ' * len(mensaje) + '\r') 
    os.sys.stdout.flush()
#---FIN FUNCIONES CONSOLA---

#---FUNCIONES BASICAS---
def agregar_usuario(lista_usuarios,bandera_editar):
    # Agrega un objeto usuario a una lista.
    os.system('cls')
    if not bandera_editar: print("\tAgregar un nuevo usuario\n")

    id = len(lista_usuarios)+1  # Se obtiene la longitud de la lista de usuarios.
    nombre = input("Nombre          : ")
    nombre = nombre.title()     # Para poner en mayuscula cada palabra del nombre.

    # Se válida que se ingresen los datos numericos correctamente.
    while True:
        try:
            edad = int(input("Edad (15-80)    : "))
            if 15 < edad < 81:
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
    # --------------------------------------------------------

    domicilio = input("Domicilio       : ")
    domicilio = domicilio.capitalize() # Para poner en mayuscula la primer letra de la cadena.
    usuario_nuevo = User(id, nombre, edad, domicilio, saldo) # Se crea un nuevo usuario con los datos asignados anteriormente.

    # Esta condición es para verificar que estamos en la función de agregar usuario, puesto que la función de modificar usuario
    # comparte esta misma función, por temas de no repetir código.
    if not bandera_editar:
        lista_usuarios.append(usuario_nuevo) # Agregamos un nuevo usuario a la lista.

        print("\tSe agregó el usuario ",nombre," correctamente\n")
        limpiar_pantalla()
        return lista_usuarios # Si estamos en la opción de agregar usuario.
    
    else:
        return usuario_nuevo  # Si estamos en la opción de editar usuario.

def agregar_articulo(lista_articulos,bandera_editar):
    os.system('cls')
    if not bandera_editar: print("\tAgregar un nuevo artículo\n")

    id = len(lista_articulos)+1 # Se obtiene la longitud de la lista de artículos.
    nombre = input("Nombre             : ")
    nombre = nombre.title() # Se pone en mayusculas todas las palabras de la cadena de texto.

    # Se válida que los datos numericos se ingresen correctamente.
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
    # -------------------------------------------------------------------

    proveedor = input("Proveedor          : ")
    proveedor.capitalize() # Para colocar en mayuscula la primer letra de la cadena.
        
    articulo_nuevo = Item(id,nombre,precio,cantidad,proveedor) # Se crea un nuevo objeto de la clase ítem.

    if not bandera_editar:
        lista_articulos.append(articulo_nuevo) # Se agrega un nuevo usuario en la lista de artículos.

        print("\tSe agregó el artículo ",nombre," correctamente\n")
        limpiar_pantalla()
        return lista_articulos # Si estamos en la opción de agregar artículo.
    
    else:
        return articulo_nuevo  # Si estamos en la opción de editar artículo.

def editar_usuario(lista_usuarios):
    aux_indice_existente = False    # Se crea una variable para validar que el índice existe.

    if not validar_arreglo_vacio(lista_usuarios): # Se verifica primero que la lista no está vacía.
        os.system('cls')
        print("\tEditar usuario\n")

        while True:
            # Se muestran los diferentes usuarios y se válida que se ingrese un índice válido dentro del rango de valores.
            try:
                mostrar_lista(lista_usuarios,0)
                indice = int(input("Ingresa el id para editar: "))
                if 0 <= indice <= len(lista_usuarios):
                    break
                else:
                    mensajes(1)
            except Exception:
                mensajes(0)
            # -------------------------------------------------------------

        # Se busca el índice en la lista de usuarios, una vez encontrado se rompe el bucle.
        for usuario in lista_usuarios:
            if usuario.get_id() == indice:
                aux_indice_existente = True
                break
        # ----------------------------------------------------------------------

        # Se válida que exista el índice ingresado anteriormente.
        if aux_indice_existente:
            aux_objeto_usuario = agregar_usuario(lista_usuarios,True) # Se obtiene el objeto del usuario con el índice ingresado.
            # Se modifican los datos del objeto.
            lista_usuarios[indice-1].set_nombre(aux_objeto_usuario.get_nombre())   
            lista_usuarios[indice-1].set_edad(aux_objeto_usuario.get_edad())     
            lista_usuarios[indice-1].set_saldo(aux_objeto_usuario.get_saldo())    
            lista_usuarios[indice-1].set_domicilio(aux_objeto_usuario.get_domicilio())
            # ----------------------------------------------------------------------------

            print("\tSe actualizó un usuario correctamente\n")
            limpiar_pantalla()
        else:
            mensajes(0)
            limpiar_pantalla()
    return lista_usuarios

def editar_articulo(lista_articulos):
    aux_indice_existente = False    # Se crea una variable para validar que el índice existe.

    if not validar_arreglo_vacio(lista_articulos): # Se verifica primero que la lista no está vacía.
        os.system('cls')
        print("\tEditar artículo\n")

        while True:
            # Se muestran los diferentes artículos y se válida que se ingrese un índice válido dentro del rango de valores.
            try:
                mostrar_lista(lista_articulos,1)
                indice = int(input("Ingresa el id para editar: "))
                if 0 <= indice <= len(lista_articulos):
                    break
                else:
                    mensajes(1)
            except Exception:
                mensajes(0)
            # -----------------------------------------------------------

        # Se busca el índice en la lista de artículos, una vez encontrado se rompe el bucle.
        for articulo in lista_articulos:
            if articulo.get_id() == indice:
                aux_indice_existente = True
                break
        # --------------------------------------------------------------

        # Se válida que exista el índice ingresado anteriormente.
        if aux_indice_existente:
            aux_objeto_articulo = agregar_articulo(lista_articulos,True) # Se obtiene el objeto del artículo con el índice ingresado.
            # Se modifican los datos del objeto.
            lista_articulos[indice-1].set_nombre(aux_objeto_articulo.get_nombre())
            lista_articulos[indice-1].set_precio(aux_objeto_articulo.get_precio())
            lista_articulos[indice-1].set_cantidad(aux_objeto_articulo.get_cantidad())
            lista_articulos[indice-1].set_proveedor(aux_objeto_articulo.get_proveedor())
            # ---------------------------------------------------------

            print("\tSe actualizó un artículo correctamente\n")
            limpiar_pantalla()

        else:
            os.system('cls')
            mensajes(0)
            limpiar_pantalla()
    return lista_articulos

def borrar_item(lista):
    aux_indice_existente = False # Se crea una variable para validar que el índice existe.

    if not validar_arreglo_vacio(lista): # Se verifica que la lista no está vacía.
        os.system('cls') 
        print("\tBorrar artículo")

        # Se válida que se ingrese una id correcta y dentro del rango.
        while True:
            try:
                indice = int(input("Ingresa el id para eliminar: "))
                break
            except Exception:
                mensajes(0)
        # ------------------------------------------------------------

        # Se busca el id dentro de la lista a eliminar
        for item in lista:
            if item.get_id() == indice:
                aux_indice_existente = True
                break
        # ---------------------------------------------
        
        if aux_indice_existente:
            del lista[indice-1]     # Se elimina el objeto de la lista con un valor de índice -1
            aux_indice_nuevo = 1

            for item in lista:
                item.set_id(aux_indice_nuevo)   # Se reasigna el índice de todos los objetos de la lista para mantenerlos en orden numerico.
                aux_indice_nuevo += 1

            print("\tSe borró un registro correctamente\n")
            limpiar_pantalla()

        else:
            os.system('cls')
            mensajes(0)
            limpiar_pantalla()

    return lista

def mostrar_lista(lista,tipo):
    if not validar_arreglo_vacio(lista):    # Se válida que la lista no está vacía.
        os.system('cls')
        print("\tMostrando elementos\n")

        # Se muestran los datos del objeto
        for item in lista:
            print("\tId:     ",item.get_id())       #Id y nombre son atributos iguales
            print("\tNombre: ",item.get_nombre())

            # Se específica el tipo de lista para mostrar sus correspondientes datos.
            if tipo == 0:
                print("\tEdad:      ",item.get_edad())
                print("\tDomicilio: ",item.get_domicilio())
                print("\tSaldo:     ",item.get_saldo(),"\n")
            elif tipo == 1:
                print("\tPrecio:    ",item.get_precio())
                print("\tCantidad:  ",item.get_cantidad())
                print("\tProveedor: ",item.get_proveedor(),"\n")
            # --------------------------------------------------------------

    limpiar_pantalla()
#---FIN FUNCIONES BASICAS---

#---FUNCIONES LISTAS---
def validar_arreglo_vacio(lista):
    # Se válida que la lista pasada por parámetro está vacía o no.
    if len(lista)==0:
        print("\tSin registros")
        limpiar_pantalla()
        return True
    
    return False

def opcion_comprar(lista_usuarios,lista_articulos):
    # Válida que exista al menos un usuario y un artículo.
    if not validar_arreglo_vacio(lista_articulos) and not validar_arreglo_vacio(lista_usuarios):

        # Se obtienen el total de artículos y usuarios, cantidad.
        aux_total_articulos = len(lista_articulos)
        aux_total_usuarios  = len(lista_usuarios)
        # ---------------------------------------------

        while True:
            try:
                # Se válida la elección del usuario, validando que sea el tipo de dato correcto y esté dentro del parámetro.
                mostrar_lista(lista_usuarios,0)
                indice_usuario_compra = int(input("\n\t Selecciona el id del usuario: "))
                indice_usuario_compra-=1
                if 0 <= indice_usuario_compra <= aux_total_usuarios:
                    break
                else:
                    mensajes(1)
            except Exception:
                mensajes(0)
                # ---------------------------------------------------------------------------------

        # Se obtiene el nombre y el saldo del usuario ingresado.
        aux_nombre_usuario = lista_usuarios[indice_usuario_compra].get_nombre()
        aux_saldo_usuario  = lista_usuarios[indice_usuario_compra].get_saldo()
        aux_precio_total = 0 
        # -------------------------------------------------------

        if aux_saldo_usuario > 0:
            aux_lista_total_cantidades = [] # Almacena todas las cantidades de todos los artículos.
            aux_lista_total_precios    = [] # Almacena todos los precios de todos los artículos.
            aux_lista_temporal_cantidades = [] # Se almacenará momentaneamente las cantidades ingresadas por el usuario.

            # Se obtienen las cantidades y precios de los diferentes artículos.
            for articulo in lista_articulos:
                aux_lista_total_cantidades.append(articulo.get_cantidad())
                aux_lista_total_precios.append(articulo.get_precio())
                aux_lista_temporal_cantidades.append(0)
            # ---------------------------------------------------------------

            aux_validar = False #Comprobar si existe algun articulo en el carrito

            while True:
                # Se muestra un menú para seleccionar la opción a realizar.
                os.system('cls')
                print("\n\tBienvenido ",aux_nombre_usuario, " tu saldo es: ",aux_saldo_usuario)
                print("\n\tSelecciona una opción del menú")
                print("\t1. Comprar")
                print("\t2. Ver carrito: ")
                print("\t3. Pagar")
                print("\t4. Salir")
                opcion_submenu = input("\n\tSelecciona una opción: ")
                # -----------------------------------------------------------

                if opcion_submenu == '1':
                    while True:
                        # Se válida el id del producto que sea existente y del tipo de dato correcto.
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
                        # ------------------------------------------------------------------------

                    while True:
                        # Se válida que la cantidad de artículos sea positiva.
                        try:
                            aux_cantidad_articulos_compra = int(input("\tSelecciona la cantidad del producto: "))
                            if aux_cantidad_articulos_compra > 0:
                                break
                            else:
                                mensajes(1)
                        except Exception:
                            mensajes(0)
                        # -----------------------------------------------------------------------------
                    
                    #VERIFICACIONES
                    # Se válida que no se ingrese un número mayor de cantidad a un artículo existente.
                    if aux_cantidad_articulos_compra+aux_lista_temporal_cantidades[indice_articulo_compra]>aux_lista_total_cantidades[indice_articulo_compra]:
                        os.system('cls')
                        print("\tNo puedes ingresar un número mayor de produtos a los existentes\n")
                        limpiar_pantalla()
                    # ----------------------------------------------------------------------------------

                    # Se válida que el saldo total a pagar sea suficiente.
                    elif aux_precio_total + aux_lista_total_precios[indice_articulo_compra]*aux_cantidad_articulos_compra > aux_saldo_usuario:
                        os.system('cls')
                        print("\tSaldo insuficiente\n")
                        limpiar_pantalla()
                    # ----------------------------------------------------

                    # Se agregan los artículos a una lista. Está lista será el carrito del usuario.
                    else:
                        aux_lista_temporal_cantidades[indice_articulo_compra] += aux_cantidad_articulos_compra
                        aux_precio_total += aux_lista_total_precios[indice_articulo_compra]*aux_cantidad_articulos_compra
                        print("\n\tSe han añadido un producto a tu carrito")
                        aux_validar = True  # Se hace true pues existe algún producto en el carrito.
                        limpiar_pantalla()
                    # ------------------------------------------------------------------

                elif opcion_submenu == '2':
                    # Si existe algún artículo en el carrito.
                    if aux_validar:
                        aux_suma_total_precios = 0

                        # Se muestran los datos de los artículos en el carrito.
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
                        # -------------------------------------------------------------

                elif opcion_submenu == '3':
                    if aux_validar:
                        # Válida el saldo del usuario contra el saldo total a pagar.
                        if aux_saldo_usuario - aux_precio_total < 0:
                            print("\tNo hay dinero suficiente\n")
                            limpiar_pantalla()
                        else:
                            # Asigna el nuevo saldo al usuario después de realizar la compra.
                            lista_usuarios[indice_usuario_compra].set_saldo(aux_saldo_usuario-aux_precio_total)
                            aux_indice_asigar = 0

                            # Se crea una lista y una tupla pata guardar datos. Para en un futuro utilizarlos para imprimirlos en un archivo .txt.
                            aux_lista_ticket = []
                            aux_tupla_ticket = ()

                            # Se asignan las cantidades correspondientes a los artículos.
                            for articulo in lista_articulos:
                                articulo.set_cantidad(aux_lista_total_cantidades[aux_indice_asigar]  - aux_lista_temporal_cantidades[aux_indice_asigar])
                                
                                # Se almacena el nombre, cantidad y total a pagar del artículo comprado.
                                if aux_lista_temporal_cantidades[aux_indice_asigar] > 0:
                                    aux_nombre_articulo   = lista_articulos[aux_indice_asigar].get_nombre()
                                    aux_cantidad_articulo = aux_lista_temporal_cantidades[aux_indice_asigar]
                                    aux_precio_articulo   = aux_lista_total_precios[aux_indice_asigar]*aux_lista_temporal_cantidades[aux_indice_asigar]

                                    aux_tupla_ticket = (aux_nombre_articulo,aux_cantidad_articulo,aux_precio_articulo)
                                    aux_lista_ticket.append(aux_tupla_ticket)

                                aux_indice_asigar +=1
                                # --------------------------------------------------------------------------
                            
                            print("\n\tSe ha realizado la compra correctamente")
                            # Se genera un ticket (archivo .txt)
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
    hora_actual  = datetime.now() # Se obtiene la fecha y hora actual
    mensaje = usuario+"Ticket.txt" # Se establece el nombre del archivo .txt

    with open(mensaje,'w') as archivo:  #ASEGURAR QUE EL ARCHIVO SE CIERRE DE FORMA CORRECTA -> w es permiso de escritura
        archivo.write("\tYosiCompro\n")         # Se escribe en una línea el mensaje.
        archivo.write(f"Fecha:{hora_actual}\n")

        # Se escribe en el archivo .txt el nombre, cantidad y precio de los diferentes productos comprados por el usuario.
        for articulo in lista_compra:
            archivo.write("Nombre:   "+articulo[0]+"\n")
            archivo.write("Cantidad: "+str(articulo[1])+"\n")
            archivo.write("Precio:   "+str(articulo[2])+"\n")
        # -----------------------------------------------------------------

def cargar_datos(lista_usuarios,lista_articulos):
    with open('Datos.txt', 'r') as archivo: # r es permiso de lectura.
        for linea in archivo:
            datos = linea.strip().split(", ")
            #STRIP(): ELIMINA LOS CARACTERES INNECESARIOS AL PRINCIPIO Y FINAL DE LA LINEA
            #SPLIT(): DIVIDE LA LÍNEA EN UNA LISTA, UTILIZANDO ", " COMO DELIMITADOR

            # Se obtienen datos ya precargados de un archivo .txt.
            clase = datos[0]
            if clase == "User":
                id          = int(datos[1])
                nombre      = datos[2]
                edad        = int(datos[3])
                domicilio   = datos[4]
                saldo       = float(datos[5])

                usuario = User(id,nombre,edad,domicilio,saldo) # Se crea un objeto usuario con los datos extraídos anteriormente.
                lista_usuarios.append(usuario)  # Se agrega el usuario a la lista.
            
            elif clase == "Item":
                id          = int(datos[1])
                nombre      = datos[2]
                precio      = float(datos[3])
                cantidad    = int(datos[4])
                proveedor   = datos[5]

                item = Item(id,nombre,precio,cantidad,proveedor) # Se crea un objeto artículo con los datos extraídos anteriormente.
                lista_articulos.append(item)    # Se agrega el artículo a la lista.

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