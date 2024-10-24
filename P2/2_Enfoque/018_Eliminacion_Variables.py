from os import system

# Definimos las probabilidades
P_A = {True: 0.6, False: 0.4}                       # P(A)
P_B_given_A = {True: {True: 0.7, False: 0.3},       # P(B | A)
                False: {True: 0.2, False: 0.8}}     # P(B | ¬A)
P_C_given_B = {True: {True: 0.9, False: 0.1},       # P(C | B)
                False: {True: 0.1, False: 0.9}}     # P(C | ¬B

def eliminar_variables(P_A, P_B_given_A, P_C_given_B, query, evidence):
    # Inicializamos la probabilidad total de la variable de interés (C)
    P_C_total = 0.0
    
    # Iteramos sobre todos los valores posibles de A
    for a in [True, False]:
        # Probabilidad de A, dada la evidencia (en este caso, no hay evidencia)
        p_a = P_A[a]
        
        # Iteramos sobre todos los valores posibles de B
        for b in [True, False]:
            # Si hay evidencia sobre B, verificamos si coincide
            if 'B' in evidence and evidence['B'] != b:
                continue
            
            # Probabilidad de B dado A
            p_b_given_a = P_B_given_A[a][b]
            
            # Calculamos la probabilidad de C
            for c in [True, False]:
                # Probabilidad de C dado B
                p_c_given_b = P_C_given_B[b][c]
                
                # Actualizamos la probabilidad total de C
                P_C_total += p_a * p_b_given_a * p_c_given_b * (1 if 'C' not in evidence else (1 if evidence['C'] == c else 0))
    
    return P_C_total

# Definimos la consulta y la evidencia
query = 'C'
evidence = {'A': True}  # Por ejemplo, A es verdadero

# Ejecutamos la eliminación de variables
probabilidad_C = eliminar_variables(P_A, P_B_given_A, P_C_given_B, query, evidence)
system('cls')
print(f"P({query} | A=True) = {probabilidad_C:.4f}")
