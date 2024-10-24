from os import system

# Probabilidades individuales
P_A = {True: 0.7, False: 0.3}  # P(A): Probabilidad de que el estudiante estudie

# P(B|A): Probabilidad de que el estudiante esté cansado dado que estudió o no
P_B_dado_A = {
    True: {True: 0.4, False: 0.6},   # Si el estudiante estudió
    False: {True: 0.9, False: 0.1}   # Si el estudiante no estudió
}

# P(C|A,B): Probabilidad de que el estudiante pase el examen dado que estudió y está cansado
P_C_dado_AyB = {
    (True, True):   {True: 0.3, False: 0.7},    # Estudió y está cansado
    (True, False):  {True: 0.9, False: 0.1},    # Estudió y no está cansado
    (False, True):  {True: 0.2, False: 0.8},    # No estudió y está cansado
    (False, False): {True: 0.5, False: 0.5}     # No estudió y no está cansado
}

def probabilidad_conjunta(P_A, P_B_dado_A, P_C_dado_AyB):
    prob_conjunta = 0
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                p_a = P_A[a]
                p_b_given_a = P_B_dado_A[a][b]
                p_c_given_a_b = P_C_dado_AyB[(a, b)][c]
                prob_conjunta += p_a * p_b_given_a * p_c_given_a_b
                print(f'P(A={a}, B={b}, C={c}) = {p_a * p_b_given_a * p_c_given_a_b:.4f}')
    return prob_conjunta

# Calcular la probabilidad conjunta
probabilidad_total = probabilidad_conjunta(P_A, P_B_dado_A, P_C_dado_AyB)
system('cls')
print(f'La probabilidad conjunta total es: {probabilidad_total:.4f}')
