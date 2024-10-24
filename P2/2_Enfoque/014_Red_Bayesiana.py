from os import system

# Probabilidad de que llueva
P_Lluvia = {True: 0.2, False: 0.8}

# Probabilidad de que el aspersor esté encendido dado que está lloviendo o no
P_Aspersor_dado_Lluvia = {
    True: {True: 0.01, False: 0.99},   # Si está lloviendo
    False: {True: 0.4, False: 0.6}     # Si no está lloviendo
}

# Probabilidad de que la hierba esté mojada dado que llueva o el aspersor esté encendido
P_HierbaMojada_dado_Lluvia_y_Aspersor = {
    (True, True):   {True: 0.99, False: 0.01},   # Llueve y aspersor encendido
    (True, False):  {True: 0.9, False: 0.1},    # Llueve y aspersor apagado
    (False, True):  {True: 0.8, False: 0.2},    # No llueve y aspersor encendido
    (False, False): {True: 0.0, False: 1.0}    # No llueve y aspersor apagado
}

def probabilidad_jerba_mojada(P_HierbaMojada, P_Aspersor, P_Lluvia):
    prob = 0
    for lluvia in [True, False]:
        for aspersor in [True, False]:
            p_w_given_rs = P_HierbaMojada[(lluvia, aspersor)][True]
            p_s_given_r = P_Aspersor_dado_Lluvia[lluvia][aspersor]
            p_r = P_Lluvia[lluvia]
            prob += p_w_given_rs * p_s_given_r * p_r
    return prob

# Calcular P(W=True)
P_W = probabilidad_jerba_mojada(P_HierbaMojada_dado_Lluvia_y_Aspersor, P_Aspersor_dado_Lluvia, P_Lluvia)

# Calcular P(R=True | W=True) usando el Teorema de Bayes
def probabilidad_lluvia_dado_jerba_mojada(P_W, P_HierbaMojada, P_Aspersor, P_Lluvia):
    p_w_given_r_true = 0
    for aspersor in [True, False]:
        p_w_given_rs = P_HierbaMojada[(True, aspersor)][True]
        p_s_given_r = P_Aspersor_dado_Lluvia[True][aspersor]
        p_r = P_Lluvia[True]
        p_w_given_r_true += p_w_given_rs * p_s_given_r * p_r
    
    # P(R=True | W=True) = (P(W=True | R=True) * P(R=True)) / P(W=True)
    return p_w_given_r_true / P_W

# Resultado: Probabilidad de que esté lloviendo dado que la hierba está mojada
P_R_given_W = probabilidad_lluvia_dado_jerba_mojada(P_W, P_HierbaMojada_dado_Lluvia_y_Aspersor, P_Aspersor_dado_Lluvia, P_Lluvia)
system('cls')
print(f"La probabilidad de que esté lloviendo dado que la hierba está mojada es: {P_R_given_W:.4f}")
