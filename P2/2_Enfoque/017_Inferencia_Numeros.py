from os import system

# Definimos las probabilidades
P_A = {True: 0.6, False: 0.4}                       # P(A)
P_B_given_A = {True: {True: 0.7, False: 0.3},       # P(B | A)
                False: {True: 0.2, False: 0.8}}     # P(B | ¬A)
P_C_given_B = {True: {True: 0.9, False: 0.1},       # P(C | B)
                False: {True: 0.1, False: 0.9}}     # P(C | ¬B

def inferencia_por_enum(P_A, P_B_given_A, P_C_given_B):
    # Inicializamos la probabilidad total de C
    P_C_total = {True: 0, False: 0}
    
    # Iteramos sobre todos los valores posibles de A
    for a in [True, False]:
        # Obtenemos la probabilidad de A
        p_a = P_A[a]
        
        # Iteramos sobre todos los valores posibles de B
        for b in [True, False]:
            # Obtenemos la probabilidad de B dado A
            p_b_given_a = P_B_given_A[a][b]
            
            # Obtenemos la probabilidad de C dado B
            p_c_given_b = P_C_given_B[b]
            
            # Actualizamos la probabilidad total de C
            for c in [True, False]:
                P_C_total[c] += p_a * p_b_given_a * p_c_given_b[c]
    
    return P_C_total

# Ejecutamos la inferencia
resultados = inferencia_por_enum(P_A, P_B_given_A, P_C_given_B)
system('cls')
print(f"P(C=True)   = {resultados[True]:.4f}")
print(f"P(C=False)  = {resultados[False]:.4f}")
