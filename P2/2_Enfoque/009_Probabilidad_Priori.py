from os import system

def probabilidad_aprobar(prior_aprobar, prior_reprobar, prob_estudiar, prob_aprobar_estudiando, prob_aprobar_no_estudiando):
    #Calcula la probabilidad a priori de aprobar un examen en función de si el estudiante estudió o no.
    
    # Calcular la probabilidad total de aprobar
    probabilidad_aprobar = (prob_estudiar * prob_aprobar_estudiando) + ((1 - prob_estudiar) * prob_aprobar_no_estudiando)
    return probabilidad_aprobar

# Parámetros
system('cls')
prior_aprobar   = 0.7  # P(A)
prior_reprobar  = 0.3  # P(R)
prob_estudiar   = 0.8  # P(E)
prob_aprobar_estudiando     = 0.9  # P(A|E)
prob_aprobar_no_estudiando  = 0.4  # P(A|¬E)

# Calcular la probabilidad a priori
probabilidad = probabilidad_aprobar(prior_aprobar, prior_reprobar, prob_estudiar, prob_aprobar_estudiando, prob_aprobar_no_estudiando)

print(f"La probabilidad a priori de aprobar el examen es: {probabilidad:.4f}")
