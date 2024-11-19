import random
import networkx as nx
import matplotlib.pyplot as plt
from os import system

class Grafo:
    def __init__(self, nodos):
        self.nodos = nodos
        self.grafo = []
    
    def agregar_arista(self, nodo1, nodo2, peso):
        self.grafo.append((peso, nodo1, nodo2))
    
    def mostrar_grafo_completo(self):
        G = nx.Graph()
        for _, nodo1, nodo2 in self.grafo:
            G.add_edge(nodo1, nodo2, weight=_)

        plt.figure(figsize=(8, 6))
        posiciones = nx.spring_layout(G)
        nx.draw(G, posiciones, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

        edge_labels = {(nodo1, nodo2): peso for peso, nodo1, nodo2 in self.grafo}
        nx.draw_networkx_edge_labels(G, posiciones, edge_labels=edge_labels)
        plt.title("Grafo completo con pesos en las aristas")
        plt.show()

    def kruskal(self, tipo="minimo"):
        # Ordenar aristas de acuerdo al peso (ascendente para mínimo, descendente para máximo)
        aristas_ordenadas = sorted(self.grafo, reverse=(tipo == "maximo"))
        padres = {nodo: nodo for nodo in self.nodos}
        rango = {nodo: 0 for nodo in self.nodos}

        def find(nodo):
            if padres[nodo] != nodo:
                padres[nodo] = find(padres[nodo])
            return padres[nodo]

        def union(nodo1, nodo2):
            raiz1 = find(nodo1)
            raiz2 = find(nodo2)

            if raiz1 != raiz2:
                if rango[raiz1] > rango[raiz2]:
                    padres[raiz2] = raiz1
                elif rango[raiz1] < rango[raiz2]:
                    padres[raiz1] = raiz2
                else:
                    padres[raiz2] = raiz1
                    rango[raiz1] += 1

        mst = []
        G = nx.Graph()
        for nodo in self.nodos:
            G.add_node(nodo)

        posiciones = nx.spring_layout(G)

        plt.figure(figsize=(8, 6))
        plt.title("Árbol")
        for peso, nodo1, nodo2 in aristas_ordenadas:
            if find(nodo1) != find(nodo2):
                union(nodo1, nodo2)
                mst.append((nodo1, nodo2, peso))
                self.mostrar_mst_en_proceso(G, mst, posiciones)
                
        return mst

    def mostrar_mst_en_proceso(self, G, mst, posiciones):
        plt.clf()
        nx.draw(G, posiciones, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

        for nodo1, nodo2, peso in mst:
            G.add_edge(nodo1, nodo2, weight=peso)

        mst_edges = [(nodo1, nodo2) for nodo1, nodo2, _ in mst]
        nx.draw_networkx_edges(G, posiciones, edgelist=mst_edges, edge_color='blue', width=2)

        edge_labels = {(nodo1, nodo2): peso for nodo1, nodo2, peso in mst}
        nx.draw_networkx_edge_labels(G, posiciones, edge_labels=edge_labels)

        plt.pause(1)

# Función para limpiar la pantalla
def limpiar_pantalla(apretar=False, limpiar=True):
    if apretar:
        input("Ingresa una tecla para continuar...")

    if limpiar:
        system('cls')

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

if __name__ == "__main__":
    cargar_datos = True
    ubicaciones = []
    caminos = []

    if cargar_datos:
        ubicaciones = ['A', 'B', 'C', 'D', 'E']
        caminos = [('A', 'B', valor_aleatorio()), ('A', 'C', valor_aleatorio()),
                ('B', 'C', valor_aleatorio()), ('B', 'D', valor_aleatorio()),
                ('C', 'D', valor_aleatorio()), ('C', 'E', valor_aleatorio()),
                ('D', 'E', valor_aleatorio())]
        
        grafo = Grafo(ubicaciones)
        for nodo1, nodo2, peso in caminos:
            grafo.agregar_arista(nodo1, nodo2, peso)

    else:
        # Si cargar_datos es False, se ingresan manualmente los datos
        ubicaciones = ingresar_ubicacion(ubicaciones)
        grafo = Grafo(ubicaciones)

        caminos = ingresar_caminos(grafo, ubicaciones, caminos)
    
    # Mostrar grafo completo antes de seleccionar el tipo de árbol
    grafo.mostrar_grafo_completo()

    tipo_arbol = "minimo"
    for _ in range(2):
        mst = grafo.kruskal(tipo_arbol)
        
        print(f"Árbol de Expansión {'Mínima' if tipo_arbol == 'minimo' else 'Máxima'} (Kruskal):")
        for arista in mst:
            print(f"{arista[0]} - {arista[1]} con peso {arista[2]}")
    
        plt.title(f"Árbol de Expansión {'Mínima' if tipo_arbol == 'minimo' else 'Máxima'} (Kruskal):")
        plt.show()
        tipo_arbol = "maximo"