import matplotlib.pyplot as plt
import networkx as nx
import random
from os import system

# Función para limpiar la pantalla
def limpiar_pantalla(apretar=False, limpiar=True):
    if apretar:
        input("Ingresa una tecla para continuar...")  # Espera una tecla para continuar

    if limpiar:
        system('cls')  # Limpia la pantalla (para Windows)

# Genera un valor aleatorio para asignar un peso/coste a las aristas
def valor_aleatorio():
    return random.randint(1, 10)

# Función para ingresar ubicaciones (nodos) de forma interactiva
def ingresar_ubicacion(ubicaciones):
    ubicacion = ''

    while ubicacion != 'S':
        print("Ingresa una ubicación o presiona -> S <- para salir")
        ubicacion = input("Ingresa una ubicación: ").capitalize()

        if ubicacion != 'S':
            ubicaciones.append(ubicacion)  # Agrega la ubicación a la lista de ubicaciones
            print(f"\nSe ha ingresado {ubicacion} correctamente")
            limpiar_pantalla(True)  # Limpia la pantalla tras cada ingreso
    return ubicaciones

# Asocia índices con ubicaciones para mostrar un menú numerado
def indice_ubicaciones(ubicaciones):
    return [(indice + 1, valor) for indice, valor in enumerate(ubicaciones)]

# Muestra la lista de ubicaciones junto con sus índices
def mostrar_ubicaciones(ubicaciones, hiden=None):
    ubicaciones_indice = indice_ubicaciones(ubicaciones)
    print("\nMostrando las diferentes ubicaciones")

    for ubicacion in ubicaciones_indice:
        if ubicacion[1] == hiden:  # Evita mostrar una ubicación específica
            continue
        print("\t", ubicacion)

# Agrega nodos y aristas al grafo desde una lista de caminos
def ingresar_grafo(Grafo, caminos):
    Grafo.add_nodes_from(Grafo.nodes)
    Grafo.add_weighted_edges_from(caminos)
    return Grafo

# Muestra el grafo visualmente con pesos en las aristas
def mostrar_grafico(Grafo, caminos=None, selector=False):
    if selector:
        Grafo.add_weighted_edges_from(caminos)  # Agrega aristas con peso
        pos = nx.spring_layout(Grafo)           # Posición de los nodos
        nx.draw(Grafo, pos, node_color='cyan', node_size=300, font_size=10, width=2, with_labels=True)
        edge_labels = nx.get_edge_attributes(Grafo, 'weight')
        nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels)

    else:
        pos = nx.spring_layout(Grafo)
        # Crear una figura con dos subplots (2 columnas)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Grafo completo
        nx.draw(Grafo, pos, ax=ax1, node_color='cyan', node_size=300, font_size=10, width=2, with_labels=True)
        edge_labels = nx.get_edge_attributes(Grafo, 'weight')
        nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels, ax=ax1)
        ax1.set_title("Grafo Completo")


        # Camino más corto
        destino = nx.DiGraph()
        for i in range(len(caminos) - 1):
            destino.add_edge(caminos[i], caminos[i + 1])

        nx.draw(destino, pos, ax=ax2, node_color='lightgreen', node_size=300, font_size=10, width=2, with_labels=True, edge_color="tab:red")
        ax2.set_title("Camino Más Corto")

    plt.show()

# Permite ingresar caminos (aristas) entre ubicaciones, asegurando que no se repitan
def ingresar_caminos(Grafo, ubicaciones, caminos):
    valores = set()  # Conjunto para registrar combinaciones de ubicaciones conectadas

    for i in range(len(ubicaciones)):
        limpiar_pantalla()
        valor = 's'

        while valor != 'S':
            print(f"Ubicacion {i + 1}: {ubicaciones[i]}")
            print(f"Selecciona el número de ubicación con la que colinda {ubicaciones[i]}")

            mostrar_ubicaciones(ubicaciones, ubicaciones[i])
            print("\nIngresa las ubicaciones o presiona ->S<- para ir a la siguiente ubicación")
            valor = input("Selecciona el índice de la ubicación donde colinda: ").capitalize()

            if valor.isnumeric():
                valor = int(valor) - 1  # Convierte el índice ingresado

                if valor != i and 0 <= valor < len(ubicaciones):
                    # Verifica que la arista (i, valor) o (valor, i) no exista en ambos sentidos
                    if (i, valor) not in valores and (valor, i) not in valores:
                        valores.add((i, valor))  # Agrega la conexión al conjunto
                        aux_tupla = (ubicaciones[i], ubicaciones[valor], valor_aleatorio())  # Define la arista
                        caminos.append(aux_tupla)  # Agrega la arista a la lista de caminos
                        print(f"{ubicaciones[i]} se ha conectado con {ubicaciones[valor]} correctamente")
                        mostrar_grafico(Grafo, caminos, True)  # Muestra el grafo actualizado
                        limpiar_pantalla(True)

                    else:
                        limpiar_pantalla()
                else:
                    print("No puedes asignar la misma ubicación o se ingresó un número inválido")
                    limpiar_pantalla(True)
    return caminos

# ETAPA 1: CONSTRUCCIÓN DEL GRAFO
limpiar_pantalla()
Grafo = nx.Graph()      # Grafo no dirigido
cargar_datos = True     # Indica si se debe cargar datos de prueba

ubicaciones = []        # Lista de nodos
caminos = []            # Lista de aristas con pesos

if cargar_datos:
    # Si cargar_datos es True, se define un grafo predeterminado
    ubicaciones = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    caminos     = [('A', 'B', valor_aleatorio()), ('A', 'F', valor_aleatorio()), ('A', 'I', valor_aleatorio()),
            ('B', 'C', valor_aleatorio()), ('B', 'E', valor_aleatorio()),
            ('C', 'D', valor_aleatorio()), ('C', 'E', valor_aleatorio()),
            ('D', 'G', valor_aleatorio()), ('D', 'H', valor_aleatorio()),
            ('E', 'G', valor_aleatorio()),
            ('F', 'G', valor_aleatorio())]
else:
    # Si cargar_datos es False, se ingresan manualmente los datos
    ubicaciones = ingresar_ubicacion(ubicaciones)
    caminos = ingresar_caminos(Grafo, ubicaciones, caminos)

limpiar_pantalla()
print("El gráfico ha quedado de la siguiente manera")
mostrar_grafico(Grafo, caminos, True)  # Muestra el grafo final construido

for x in caminos:
    print("\t", x)
limpiar_pantalla(True)

# ETAPA 2: OBTENER EL CAMINO MÁS CORTO
Grafo = ingresar_grafo(Grafo, caminos)  # Construye el grafo con las aristas y pesos definidos
destino = nx.DiGraph()                  # Grafo dirigido para mostrar el camino más corto

# Solicita al usuario el inicio y fin del trayecto
while True:
    mostrar_ubicaciones(ubicaciones)
    inicio = int(input("\nIngresa el inicio del trayecto (SOLO EL NÚMERO): ")) - 1
    fin    = int(input("Ingresa el fin    del trayecto (SOLO EL NÚMERO): ")) - 1

    if inicio != fin and 0 <= inicio < len(ubicaciones) and 0 <= fin < len(ubicaciones):
        print(f"Inicio {ubicaciones[inicio]} <-> Destino {ubicaciones[fin]}")
        limpiar_pantalla(True)
        break
    else:
        print("Se ha ingresado un valor repetido o se ha ingresado un valor inválido")

# Calcula el camino más corto y el costo total usando Dijkstra
best = nx.dijkstra_path(Grafo, ubicaciones[inicio], ubicaciones[fin])
costo_total = nx.dijkstra_path_length(Grafo, ubicaciones[inicio], ubicaciones[fin])

# Muestra el camino más corto y su costo total
print(f"El camino más corto de {ubicaciones[inicio]} a {ubicaciones[fin]} es: {best} y el costo es: {costo_total}")
mostrar_grafico(Grafo, best)
# FIN ETAPA 2