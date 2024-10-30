import numpy as np

# Clase para construir el arbol de regresion M5
class NodoM5:
    def __init__(self, columna=None, valor=None, izquierdo=None, derecho=None, resultado=None):
        self.columna = columna
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.resultado = resultado

# Funcion para dividir el conjunto de datos segun la columna y el valor de division
def dividir_datos(datos, columna, valor):
    izquierdo = datos[datos[:, columna] <= valor]
    derecho = datos[datos[:, columna] > valor]
    return izquierdo, derecho

# Funcion para calcular el error de una division (desviacion estandar)
def error(datos):
    if len(datos) == 0:
        return 0
    return np.var(datos[:, -1]) * len(datos)

# Funcion para encontrar la mejor division para minimizar el error
def mejor_division(datos):
    mejor_error = float('inf')
    mejor_columna, mejor_valor = None, None
    for columna in range(datos.shape[1] - 1):
        valores = np.unique(datos[:, columna])
        for valor in valores:
            izquierdo, derecho = dividir_datos(datos, columna, valor)
            if len(izquierdo) > 0 and len(derecho) > 0:
                error_division = error(izquierdo) + error(derecho)
                if error_division < mejor_error:
                    mejor_error, mejor_columna, mejor_valor = error_division, columna, valor
    return mejor_columna, mejor_valor

# Funcion para construir el arbol de regresion M5
def construir_arbol(datos, min_tamano=5):
    if len(datos) <= min_tamano:
        return NodoM5(resultado=np.mean(datos[:, -1]))
    columna, valor = mejor_division(datos)
    if columna is None:
        return NodoM5(resultado=np.mean(datos[:, -1]))
    izquierdo, derecho = dividir_datos(datos, columna, valor)
    nodo_izquierdo = construir_arbol(izquierdo, min_tamano)
    nodo_derecho = construir_arbol(derecho, min_tamano)
    return NodoM5(columna=columna, valor=valor, izquierdo=nodo_izquierdo, derecho=nodo_derecho)

# Funcion para predecir usando el arbol de regresion M5
def predecir(arbol, fila):
    if arbol.resultado is not None:
        return arbol.resultado
    if fila[arbol.columna] <= arbol.valor:
        return predecir(arbol.izquierdo, fila)
    else:
        return predecir(arbol.derecho, fila)

# Conjunto de datos de ejemplo
datos = np.array([
    [5, 10, 20],
    [10, 15, 30],
    [15, 20, 45],
    [20, 25, 50],
    [25, 30, 65],
    [30, 35, 80],
    [35, 40, 95],
    [40, 45, 110]
])

# Construccion del arbol M5
arbol = construir_arbol(datos)

# Prediccion de un nuevo valor
nueva_fila = np.array([23, 10])  # Fila de ejemplo (sin el valor objetivo)
prediccion = predecir(arbol, nueva_fila)

# Mostrar resultado
print("Prediccion para la entrada {}: {:.2f}".format(nueva_fila, prediccion))