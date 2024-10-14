class Nodo:
    def __init__(self, nombre, es_and=False):
        self.nombre = nombre
        self.es_and = es_and
        self.hijos = []  # lista de (nodo, costo) para representar los nodos hijos y su costo
        self.solucionado = False
        self.costo = float('inf')  # Costo inicial

    def agregar_hijo(self, nodo, costo):
        self.hijos.append((nodo, costo))

class BusquedaAOEstrella:
    def __init__(self, heuristicas):
        self.heuristicas = heuristicas

    def ao_estrella(self, nodo):
        if nodo.solucionado:
            return nodo.costo

        # Si es un nodo hoja (sin hijos), devolver la heurística
        if not nodo.hijos:
            nodo.costo = self.heuristicas[nodo.nombre]
            nodo.solucionado = True
            return nodo.costo

        # Si es un nodo AND, necesitamos resolver todos los hijos
        if nodo.es_and:
            nodo.costo = 0
            for hijo, costo in nodo.hijos:
                nodo.costo += self.ao_estrella(hijo) + costo
        # Si es un nodo OR, elegimos el hijo con el menor costo
        else:
            mejores_costos = []
            for hijo, costo in nodo.hijos:
                costo_total = self.ao_estrella(hijo) + costo
                mejores_costos.append(costo_total)
            nodo.costo = min(mejores_costos)

        nodo.solucionado = True
        return nodo.costo

# Heurísticas (estimaciones)
heuristicas = {
    'A': 10,
    'B': 5,
    'C': 4,
    'D': 7,
    'E': 3,
    'F': 0  # Nodo objetivo tiene costo 0
}

# Construir el grafo AND-OR
nodo_A = Nodo('A')
nodo_B = Nodo('B', es_and=True)
nodo_C = Nodo('C')
nodo_D = Nodo('D')
nodo_E = Nodo('E')
nodo_F = Nodo('F')

nodo_A.agregar_hijo(nodo_B, 1)
nodo_A.agregar_hijo(nodo_C, 3)

nodo_B.agregar_hijo(nodo_D, 2)
nodo_B.agregar_hijo(nodo_E, 2)

nodo_C.agregar_hijo(nodo_F, 4)
nodo_E.agregar_hijo(nodo_F, 3)

# Ejecutar AO*
busqueda_ao_estrella = BusquedaAOEstrella(heuristicas)
costo_optimo = busqueda_ao_estrella.ao_estrella(nodo_A)
print(f"Costo óptimo desde el nodo A: {costo_optimo}")
