from os import system

# Implementación de la búsqueda tabú
class BusquedaTabu:
    def __init__(self, grafo, heuristica, max_tabu_size=5, max_iteraciones=50):
        self.grafo = grafo
        self.heuristica = heuristica
        self.max_tabu_size = max_tabu_size
        self.max_iteraciones = max_iteraciones
        self.lista_tabu = []

    def busqueda_tabu(self, inicio, objetivo):
        nodo_actual = inicio
        mejor_nodo = nodo_actual
        mejor_heuristica = self.heuristica[nodo_actual]
        camino = [nodo_actual]

        for iteracion in range(self.max_iteraciones):
            vecinos = self.grafo[nodo_actual]

            mejor_vecino = None
            mejor_vecino_heuristica = float('inf')

            # Explorar todos los vecinos
            for vecino, _ in vecinos:
                if vecino not in self.lista_tabu and self.heuristica[vecino] < mejor_vecino_heuristica:
                    mejor_vecino = vecino
                    mejor_vecino_heuristica = self.heuristica[vecino]

            # Si encontramos un vecino mejor, avanzamos hacia él
            if mejor_vecino is not None:
                nodo_actual = mejor_vecino
                camino.append(nodo_actual)

                # Actualizamos el mejor nodo encontrado
                if mejor_vecino_heuristica < mejor_heuristica:
                    mejor_nodo = mejor_vecino
                    mejor_heuristica = mejor_vecino_heuristica

                # Añadimos el nodo a la lista tabú
                self.lista_tabu.append(nodo_actual)
                if len(self.lista_tabu) > self.max_tabu_size:
                    self.lista_tabu.pop(0)  # Eliminamos el nodo más antiguo si la lista supera el tamaño permitido

                # Si alcanzamos el objetivo, retornamos el camino
                if nodo_actual == objetivo:
                    print(f"Objetivo encontrado en la iteración {iteracion + 1}")
                    return camino
            else:
                # Si no hay vecinos válidos, detener
                print("No hay más vecinos válidos para explorar.")
                break

        print(f"Objetivo no encontrado después de {self.max_iteraciones} iteraciones.")
        return camino if camino[-1] == objetivo else None

# Grafo representado como un diccionario (lista de adyacencia con costos)
system('cls')
grafo = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heurística (estimación cuán lejos está cada nodo del objetivo 'F')
heuristica = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 0
}

# Crear el objeto de búsqueda tabú
busqueda = BusquedaTabu(grafo, heuristica, max_tabu_size=3, max_iteraciones=20)

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

# Ejemplo de búsqueda tabú desde el nodo 'x' hasta el nodo 'y'
camino_tabu = busqueda.busqueda_tabu(nodo_inicio, nodo_final)
print(f"Camino encontrado con búsqueda tabú: {camino_tabu}")
