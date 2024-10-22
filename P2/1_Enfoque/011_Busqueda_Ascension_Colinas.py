from os import system

# Implementación de la búsqueda de ascensión de colinas
class BusquedaAscensionColinas:
    def __init__(self, grafo, heuristica):
        self.grafo = grafo
        self.heuristica = heuristica

    def ascension_colinas(self, inicio, objetivo):
        nodo_actual = inicio
        camino = [nodo_actual]

        while nodo_actual != objetivo:
            vecinos = self.grafo[nodo_actual]
            mejor_vecino = None
            mejor_heuristica = float('inf')  # Valor grande para minimización

            # Buscar el vecino con la mejor heurística
            for vecino, _ in vecinos:
                if self.heuristica[vecino] < mejor_heuristica:
                    mejor_heuristica = self.heuristica[vecino]
                    mejor_vecino = vecino

            # Si no encontramos un vecino mejor, estamos en un máximo local
            if mejor_heuristica >= self.heuristica[nodo_actual]:
                print("Se alcanzó un máximo local.")
                return camino

            # Avanzamos al mejor vecino encontrado
            nodo_actual = mejor_vecino
            camino.append(nodo_actual)

        return camino

# Grafo representado como un diccionario (lista de adyacencia)
system('cls')
grafo = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heurística (estimar cuán lejos está cada nodo del objetivo 'F')
heuristica = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

# Crear el objeto de búsqueda de ascensión de colinas
busqueda = BusquedaAscensionColinas(grafo, heuristica)

# Ingresar el nodo de inicio
try:
    while True:
        nodo_inicio = input("Selecciona el nodo en donde comenzar  (A-F): ").upper()
        nodo_final  = input("Selecciona el nodo en donde finalizar (A-F): ").upper()

        if nodo_inicio in grafo.keys() and nodo_final in grafo.keys():
            break
        else:
            print("Valor de un nodo no está dentro del rango de valores")

except Exception:
    print("Ingresa una opción correcta")

# Ejemplo de búsqueda de ascensión de colinas desde el nodo 'A' hasta el nodo 'F'
system('cls')
camino_ascension = busqueda.ascension_colinas(nodo_inicio, nodo_final)
print(f"Camino encontrado con ascensión de colinas: {camino_ascension}")
