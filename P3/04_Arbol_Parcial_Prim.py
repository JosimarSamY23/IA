import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq
from os import system

class Grafo:
    def __init__(self, nodos):
        self.nodos = nodos
        self.grafo = {nodo: [] for nodo in nodos}

    def agregar_arista(self, nodo1, nodo2, peso):
        self.grafo[nodo1].append((nodo2, peso))
        self.grafo[nodo2].append((nodo1, peso))

    def mostrar_grafo_completo(self):
        # Inicializa el grafo de NetworkX y agrega los nodos y aristas
        G = nx.Graph()
        for nodo in self.grafo:
            G.add_node(nodo)
        for nodo in self.grafo:
            for vecino, peso in self.grafo[nodo]:
                G.add_edge(nodo, vecino, weight=peso)
        
        # Dibuja el grafo completo con sus pesos
        plt.figure(figsize=(8, 6))
        posiciones = nx.spring_layout(G)  # Disposición de nodos
        nx.draw(G, posiciones, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
        
        # Etiquetas de peso en las aristas
        edge_labels = {(nodo1, nodo2): peso for nodo1 in self.grafo for nodo2, peso in self.grafo[nodo1]}
        nx.draw_networkx_edge_labels(G, posiciones, edge_labels=edge_labels)
        
        plt.title("Grafo completo con pesos en las aristas")
        plt.show()  # Muestra la visualización del grafo completo

    def prim(self, nodo_inicio):
        # Inicialización
        mst = []  # El árbol de expansión mínima
        visitados = set([nodo_inicio])  # Nodo inicial
        aristas = [
            (peso, nodo_inicio, vecino)
            for vecino, peso in self.grafo[nodo_inicio]
        ]
        heapq.heapify(aristas)

        # Configuración de NetworkX para el grafo completo y la visualización del MST en construcción
        G = nx.Graph()
        for nodo in self.grafo:
            G.add_node(nodo)
        for nodo in self.grafo:
            for vecino, peso in self.grafo[nodo]:
                G.add_edge(nodo, vecino, weight=peso)
        
        plt.figure(figsize=(8, 6))
        posiciones = nx.spring_layout(G)  # Define la disposición de nodos para el grafo

        while aristas:
            peso, nodo1, nodo2 = heapq.heappop(aristas)
            if nodo2 not in visitados:
                visitados.add(nodo2)
                mst.append((nodo1, nodo2, peso))
                self.mostrar_mst_en_proceso(G, mst, posiciones)  # Llama a la función de visualización paso a paso

                # Agregar nuevas aristas del nodo recién visitado
                for vecino, peso in self.grafo[nodo2]:
                    if vecino not in visitados:
                        heapq.heappush(aristas, (peso, nodo2, vecino))

        return mst

    def mostrar_mst_en_proceso(self, G, mst, posiciones):
        plt.clf()  # Limpia la figura
        # Dibuja el grafo completo en gris
        nx.draw(G, posiciones, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
        
        # Dibuja las aristas en el MST en azul para mostrar el progreso
        mst_edges = [(nodo1, nodo2) for nodo1, nodo2, _ in mst]
        nx.draw_networkx_edges(G, posiciones, edgelist=mst_edges, edge_color='blue', width=2)
        
        # Dibuja las etiquetas de peso en las aristas del MST
        edge_labels = {(nodo1, nodo2): peso for nodo1, nodo2, peso in mst}
        nx.draw_networkx_edge_labels(G, posiciones, edge_labels=edge_labels)
        
        plt.pause(1)  # Pausa para ver cada paso del proceso

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
                        limpiar_pantalla(True)

                    else:
                        limpiar_pantalla()
                else:
                    print("No puedes asignar la misma ubicación o se ingresó un número inválido")
                    limpiar_pantalla(True)
    return caminos

# ETAPA 1: CONSTRUCCIÓN DEL GRAFO
if __name__ == "__main__":
    limpiar_pantalla()
    cargar_datos = True     # Indica si se debe cargar datos de prueba

    ubicaciones = []        # Lista de nodos
    caminos = []            # Lista de aristas con pesos

    if cargar_datos:
        # Si cargar_datos es True, se define un grafo predeterminado
        ubicaciones = ['A', 'B', 'C', 'D', 'E']
        caminos     = [('A', 'B', valor_aleatorio()), ('A', 'C', valor_aleatorio()),
                    ('B', 'C', valor_aleatorio()), ('B', 'D', valor_aleatorio()),
                    ('C', 'D', valor_aleatorio()), ('C', 'E', valor_aleatorio()),
                    ('D', 'E', valor_aleatorio())]
        
        grafo = Grafo(ubicaciones)
        for nodo1, nodo2, peso in caminos:
            grafo.agregar_arista(nodo1,nodo2,peso)

    else:
        # Si cargar_datos es False, se ingresan manualmente los datos
        ubicaciones = ingresar_ubicacion(ubicaciones)
        grafo = Grafo(ubicaciones)

        caminos = ingresar_caminos(grafo, ubicaciones, caminos)

    print("El grafo a quedado de la siguiente manera")
    grafo.mostrar_grafo_completo()
    limpiar_pantalla(True)

    while True:
        mostrar_ubicaciones(ubicaciones)
        inicio = int(input("\nIngresa el inicio del trayecto (SOLO EL NÚMERO): ")) - 1

        if 0 <= inicio < len(ubicaciones):
            print(f"Inicio {ubicaciones[inicio]}")
            limpiar_pantalla(True)
            break

        else:
            print("Se ha ingresado un valor repetido o se ha ingresado un valor inválido")
        
    mst = grafo.prim(ubicaciones[inicio])
    for arista in mst:
        print(f"{arista[0]} - {arista[1]} con peso {arista[2]}")

    plt.show()