import numpy as np
from os import system

# Probabilidades
P_lluvia = 0.8                              # Probabilidad de que llueva
P_paraguas_dado_lluvia = 0.5                # Probabilidad de que lleve paraguas dado que llueve
P_paraguas_dado_no_lluvia = 0.1             # Probabilidad de que lleve paraguas dado que no llueve
P_mojado_dado_lluvia_y_paraguas = 0.1       # Probabilidad de que se moje dado que llueve y tiene paraguas
P_mojado_dado_lluvia_y_no_paraguas = 0.9    # Probabilidad de que se moje dado que llueve y no tiene paraguas

# Simulación del escenario
def calcular_probabilidades_condicionales():
    #Calcula probabilidades condicionales e ilustra el concepto de independencia condicional.
    
    # P(A): Probabilidad de que lleve paraguas
    P_paraguas = P_lluvia * P_paraguas_dado_lluvia + (1 - P_lluvia) * P_paraguas_dado_no_lluvia
    
    # P(B): Probabilidad de que esté mojado
    P_mojado = (P_lluvia * (P_paraguas_dado_lluvia * P_mojado_dado_lluvia_y_paraguas + 
                            (1 - P_paraguas_dado_lluvia) * P_mojado_dado_lluvia_y_no_paraguas))
    
    # P(A|C): Probabilidad de que lleve paraguas dado que llueve
    P_paraguas_cond_lluvia = P_paraguas_dado_lluvia
    
    # P(B|C): Probabilidad de que esté mojado dado que llueve
    P_mojado_cond_lluvia = (P_paraguas_dado_lluvia * P_mojado_dado_lluvia_y_paraguas + 
                            (1 - P_paraguas_dado_lluvia) * P_mojado_dado_lluvia_y_no_paraguas)
    
    # P(A ∩ B | C): Probabilidad de que lleve paraguas y esté mojado dado que llueve
    P_paraguas_y_mojado_cond_lluvia = (P_paraguas_dado_lluvia * P_mojado_dado_lluvia_y_paraguas)
    
    # Verificamos la independencia condicional: P(A ∩ B | C) ?= P(A | C) * P(B | C)
    independencia_condicional = np.isclose(
        P_paraguas_y_mojado_cond_lluvia, 
        P_paraguas_cond_lluvia * P_mojado_cond_lluvia
    )
    
    return independencia_condicional, P_paraguas_cond_lluvia, P_mojado_cond_lluvia

# Cálculo de las probabilidades
independencia_condicional, P_paraguas_cond_lluvia, P_mojado_cond_lluvia = calcular_probabilidades_condicionales()

# Resultados
system('cls')
print(f"Probabilidad de llevar paraguas dado que llueve: {P_paraguas_cond_lluvia:.4f}")
print(f"Probabilidad de estar mojado dado que llueve: {P_mojado_cond_lluvia:.4f}")
print(f"¿Independencia condicional? {'Sí' if independencia_condicional else 'No'}")
