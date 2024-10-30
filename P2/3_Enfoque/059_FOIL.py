class FOIL:
    def __init__(self):
        self.rules = []

    def train(self, examples, target):
        while True:
            rule = self.find_best_rule(examples, target)
            if rule is None:
                break
            self.rules.append(rule)
            examples = self.remove_covered_examples(examples, rule)

    def find_best_rule(self, examples, target):
        best_rule = None
        best_coverage = 0
        for example in examples:
            rule = self.create_rule(example)
            coverage = self.count_covered_examples(examples, rule, target)
            if coverage > best_coverage:
                best_coverage = coverage
                best_rule = rule
        return best_rule

    def create_rule(self, example):
        # Crea una regla a partir de un ejemplo
        return {i: val for i, val in enumerate(example[:-1])}  # Excluye el objetivo

    def count_covered_examples(self, examples, rule, target):
        count = 0
        for example in examples:
            if self.matches_rule(example, rule):
                if example[-1] == target:  # Suponiendo que el target es la última columna
                    count += 1
        return count

    def matches_rule(self, example, rule):
        # Comprueba que el ejemplo cumpla con la regla
        return all(i < len(example) and example[i] == val for i, val in rule.items())

    def remove_covered_examples(self, examples, rule):
        return [ex for ex in examples if not self.matches_rule(ex, rule)]

    def predict(self, example):
        for rule in self.rules:
            if self.matches_rule(example, rule):
                return True
        return False

# Ejemplo de datos
data = [
    [1, 'A', 1],  # Ejemplo 1
    [1, 'B', 1],  # Ejemplo 2
    [0, 'A', 0],  # Ejemplo 3
    [0, 'B', 0],  # Ejemplo 4
]

# Entrenar el modelo FOIL
foil = FOIL()
foil.train(data, 1)

# Predecir nuevos ejemplos
nuevos_ejemplos = [
    [1, 'A'],  # Ejemplo 1
    [0, 'B'],  # Ejemplo 2
    [1, 'B'],  # Ejemplo 3
    [0, 'A'],  # Ejemplo 4
    [1, 'C'],  # Ejemplo 5 (no en el conjunto de entrenamiento)
]

for ejemplo in nuevos_ejemplos:
    resultado = foil.predict(ejemplo + [None])  # Se añade un valor temporal para evitar el error de longitud
    print(f"Ejemplo {ejemplo} - Predicción: {resultado}")