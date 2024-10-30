import math
from collections import Counter

# Funcion para calcular la entropia
def calcular_entropia(datos):
    total = len(datos)
    etiquetas = [fila[-1] for fila in datos]
    frecuencia = Counter(etiquetas)
    entropia = 0
    for key in frecuencia:
        prob = frecuencia[key] / total
        entropia -= prob * math.log2(prob)
    return entropia

# Funcion para dividir los datos segun el valor del atributo
def dividir_datos(datos, indice_atributo, valor_atributo):
    subconjunto = []
    for fila in datos:
        if fila[indice_atributo] == valor_atributo:
            reducida = fila[:indice_atributo] + fila[indice_atributo + 1:]
            subconjunto.append(reducida)
    return subconjunto

# Funcion para encontrar el mejor atributo
def mejor_atributo(datos):
    num_atributos = len(datos[0]) - 1
    entropia_inicial = calcular_entropia(datos)
    mejor_ganancia = 0
    mejor_indice = 0
    for i in range(num_atributos):
        valores = set([fila[i] for fila in datos])
        entropia_atributo = 0
        for valor in valores:
            subconjunto = dividir_datos(datos, i, valor)
            prob = len(subconjunto) / len(datos)
            entropia_atributo += prob * calcular_entropia(subconjunto)
        ganancia = entropia_inicial - entropia_atributo
        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor_indice = i
    return mejor_indice

# Funcion para construir el arbol de decision
def construir_arbol(datos, etiquetas):
    etiquetas_clase = [fila[-1] for fila in datos]
    if etiquetas_clase.count(etiquetas_clase[0]) == len(etiquetas_clase):
        return etiquetas_clase[0]
    if len(datos[0]) == 1:
        return Counter(etiquetas_clase).most_common(1)[0][0]
    
    mejor_indice = mejor_atributo(datos)
    mejor_etiqueta = etiquetas[mejor_indice]
    arbol = {mejor_etiqueta: {}}
    valores = set([fila[mejor_indice] for fila in datos])
    for valor in valores:
        subconjunto = dividir_datos(datos, mejor_indice, valor)
        sub_etiquetas = etiquetas[:mejor_indice] + etiquetas[mejor_indice + 1:]
        arbol[mejor_etiqueta][valor] = construir_arbol(subconjunto, sub_etiquetas)
    return arbol

# Conjunto de datos de ejemplo
datos = [
    ['sol', 'calor', 'alta', 'si', 'no'],
    ['sol', 'calor', 'alta', 'no', 'no'],
    ['nublado', 'calor', 'alta', 'si', 'si'],
    ['lluvia', 'suave', 'alta', 'si', 'si'],
    ['lluvia', 'frio', 'normal', 'si', 'si'],
    ['lluvia', 'frio', 'normal', 'no', 'no'],
    ['nublado', 'frio', 'normal', 'no', 'si'],
    ['sol', 'suave', 'alta', 'si', 'no'],
    ['sol', 'frio', 'normal', 'si', 'si'],
    ['lluvia', 'suave', 'normal', 'si', 'si'],
    ['sol', 'suave', 'normal', 'no', 'si'],
    ['nublado', 'suave', 'alta', 'si', 'si'],
    ['nublado', 'calor', 'normal', 'no', 'si'],
    ['lluvia', 'suave', 'alta', 'no', 'no']
]
etiquetas = ['Clima', 'Temperatura', 'Humedad', 'Viento']

# Construir el arbol de decision
arbol_decision = construir_arbol(datos, etiquetas)

# Funcion para imprimir el arbol de decision
def imprimir_arbol(arbol, nivel=0):
    if isinstance(arbol, dict):
        for key, value in arbol.items():
            print("  " * nivel + str(key) + ":")
            imprimir_arbol(value, nivel + 1)
    else:
        print("  " * nivel + "->", arbol)

# Imprimir el arbol generado
print("Arbol de Decision (ID3):")
imprimir_arbol(arbol_decision)