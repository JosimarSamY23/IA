import random

# Función de aptitud que se desea maximizar
def funcion_objetivo(x):
    return x ** 2  # Maximizar f(x) = x^2

# Clase que representa un individuo en la población
class Individuo:
    def __init__(self, gen):
        self.gen = gen
        self.aptitud = funcion_objetivo(gen)

    def __str__(self):
        return f"Individuo(gen: {self.gen}, aptitud: {self.aptitud})"

# Implementación del algoritmo genético
class AlgoritmoGenetico:
    def __init__(self, tam_poblacion=10, tasas_mutacion=0.1, max_generaciones=50):
        self.tam_poblacion = tam_poblacion
        self.tasas_mutacion = tasas_mutacion
        self.max_generaciones = max_generaciones

    def crear_poblacion_inicial(self):
        return [Individuo(random.uniform(-10, 10)) for _ in range(self.tam_poblacion)]

    def seleccion(self, poblacion):
        # Selección de los mejores individuos
        poblacion.sort(key=lambda ind: ind.aptitud, reverse=True)
        return poblacion[:self.tam_poblacion // 2]  # Selecciona el 50% superior

    def cruzamiento(self, padres):
        descendencia = []
        while len(descendencia) < self.tam_poblacion:
            padre1, padre2 = random.sample(padres, 2)  # Selección aleatoria de dos padres
            hijo_gen = (padre1.gen + padre2.gen) / 2  # Cruzamiento simple (promedio)
            descendencia.append(Individuo(hijo_gen))
        return descendencia

    def mutacion(self, poblacion):
        for ind in poblacion:
            if random.random() < self.tasas_mutacion:  # Probabilidad de mutación
                ind.gen += random.uniform(-1, 1)  # Ajuste aleatorio al gen
                ind.aptitud = funcion_objetivo(ind.gen)  # Recalcular aptitud

    def ejecutar(self):
        poblacion = self.crear_poblacion_inicial()

        for generacion in range(self.max_generaciones):
            print(f"Generación {generacion + 1}:")
            for ind in poblacion:
                print(ind)

            # Selección
            padres = self.seleccion(poblacion)

            # Cruzamiento
            descendencia = self.cruzamiento(padres)

            # Mutación
            self.mutacion(descendencia)

            # Nueva población
            poblacion = padres + descendencia

        # Mejor solución encontrada
        mejor_individuo = max(poblacion, key=lambda ind: ind.aptitud)
        print(f"\nMejor individuo encontrado: {mejor_individuo}")

# Crear y ejecutar el algoritmo genético
algoritmo_gen = AlgoritmoGenetico(tam_poblacion=10, tasas_mutacion=0.1, max_generaciones=20)
algoritmo_gen.ejecutar()
