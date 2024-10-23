from os import system

def calcular_probabilidad_condicionada(bolas_rojas, bolas_azules, bolas_verdes):
    #Calcula la probabilidad de sacar una bola roja dado que se ha sacado una bola azul.

    total_bolas = bolas_rojas + bolas_azules + bolas_verdes
    prob_azul = bolas_azules / total_bolas  # P(B)
    
    # Probabilidad de sacar una bola roja y una azul (considerando reemplazo)
    prob_roja_y_azul = bolas_rojas / total_bolas * bolas_azules / total_bolas  # P(A ∩ B)

    # Aplicar la fórmula de probabilidad condicionada
    probabilidad_roja_dada_azul = prob_roja_y_azul / prob_azul

    return probabilidad_roja_dada_azul

def normalizar_probabilidades(probabilidades):
    #Normaliza una lista de probabilidades para que sumen 1.

    suma_probabilidades = sum(probabilidades)
    return [p / suma_probabilidades for p in probabilidades]

while True:
    try:
        system('cls')
        bolas_rojas  = int(input("Ingresa el número de bolas rojas  (1-5): "))
        bolas_azules = int(input("Ingresa el número de bolas azules (1-5): "))
        bolas_verdes = int(input("Ingresa el número de bolas verdes (1-5): "))

        if 0 < bolas_rojas < 6 and 0 < bolas_azules < 6 and 0 < bolas_verdes < 6:
            # Calcular probabilidad condicionada
            probabilidad = calcular_probabilidad_condicionada(bolas_rojas, bolas_azules, bolas_verdes)
            print(f"La probabilidad de sacar una bola roja dado que se ha sacado una bola azul es: {probabilidad:.4f}")

            # Calcular probabilidades de cada color
            total_bolas = bolas_rojas + bolas_azules + bolas_verdes

            probabilidades = [
                bolas_rojas  / total_bolas,  # Probabilidad de roja
                bolas_azules / total_bolas,  # Probabilidad de azul
                bolas_verdes / total_bolas   # Probabilidad de verde
            ]

            # Normalizar probabilidades
            probabilidades_normalizadas = normalizar_probabilidades(probabilidades)

            # Mostrar probabilidades normalizadas
            print("Probabilidades normalizadas:")
            print(f"Bolas rojas:  {probabilidades_normalizadas[0]:.4f}")
            print(f"Bolas azules: {probabilidades_normalizadas[1]:.4f}")
            print(f"Bolas verdes: {probabilidades_normalizadas[2]:.4f}")
            break
        else:
            print("Ingresa un valor correspondiente dentro del rango")

    except Exception:
        print("Ha ocurrido un error a la hora de ingresar los datos")