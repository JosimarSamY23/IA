from os import system

def regla_bayes(P_H, P_E_dado_H, P_E_dado_no_H):
    """
    Aplica la Regla de Bayes para calcular la probabilidad posterior de una hipótesis dada la evidencia.
    
    :param P_H: Probabilidad a priori de la hipótesis (tener la enfermedad).
    :param P_E_dado_H: Probabilidad de la evidencia dado que la hipótesis es verdadera (prueba positiva si tiene la enfermedad).
    :param P_E_dado_no_H: Probabilidad de la evidencia dado que la hipótesis es falsa (prueba positiva si no tiene la enfermedad).
    :return: Probabilidad posterior de la hipótesis dada la evidencia.
    """
    # Probabilidad de que no se tenga la enfermedad
    P_no_H = 1 - P_H
    
    # Probabilidad total de la evidencia P(E)
    P_E = P_E_dado_H * P_H + P_E_dado_no_H * P_no_H
    
    # Aplicación de la Regla de Bayes
    P_H_dado_E = (P_E_dado_H * P_H) / P_E
    
    return P_H_dado_E

# Parámetros del problema
P_H = 0.01              # Probabilidad de tener la enfermedad (1%)
P_E_dado_H = 0.99       # Probabilidad de una prueba positiva dado que tiene la enfermedad
P_E_dado_no_H = 0.05    # Probabilidad de una prueba positiva dado que NO tiene la enfermedad

# Calcular la probabilidad posterior
P_H_dado_E = regla_bayes(P_H, P_E_dado_H, P_E_dado_no_H)

# Resultado
system('cls')
print(f"La probabilidad de tener la enfermedad dado un resultado positivo es: {P_H_dado_E:.4f}")