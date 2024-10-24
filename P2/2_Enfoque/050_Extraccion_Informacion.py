import re
from os import system

# Texto de ejemplo
texto = """
El presidente de Estados Unidos, Joe Biden, visitó Francia el 24 de abril de 2021.
Microsoft anunció una nueva alianza con Google en Silicon Valley.
La NASA lanzará su próxima misión a Marte en 2024 desde Cabo Cañaveral.
"""

# Definir patrones para diferentes entidades (personas, organizaciones, lugares, fechas)
patron_personas = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
patron_organizaciones = r'\b[A-Z][a-zA-Z]+\b'
patron_lugares = r'(Estados Unidos|Francia|Silicon Valley|Cabo Cañaveral|Marte)'
patron_fechas = r'\b\d{1,2}\sde\s[A-Za-z]+\sde\s\d{4}|\d{4}'

# Función para extraer entidades basadas en los patrones
def extraer_entidades(texto):
    personas = re.findall(patron_personas, texto)
    organizaciones = re.findall(patron_organizaciones, texto)
    lugares = re.findall(patron_lugares, texto)
    fechas = re.findall(patron_fechas, texto)
    
    return {
        "Personas": personas,
        "Organizaciones": organizaciones,
        "Lugares": lugares,
        "Fechas": fechas
    }

# Extraer entidades
entidades = extraer_entidades(texto)

# Mostrar resultados
system('cls')
print("Entidades extraídas:")
for tipo, lista_entidades in entidades.items():
    print(f"\n{tipo}:")
    for entidad in lista_entidades:
        print(f"- {entidad}")
