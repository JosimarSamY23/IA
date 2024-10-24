import matplotlib.pyplot as plt
import numpy as np
from os import system

# Datos para el gráfico de líneas
x = np.linspace(0, 10, 100)  # 100 valores de 0 a 10
y = np.sin(x)  # Seno de los valores de x

# Datos para el histograma
data = np.random.randn(500)  # 1000 números aleatorios de distribución normal

# Crear una figura con 2 subplots (gráficos)
fig, axs = plt.subplots(2, 1, figsize=(8, 6))  # 2 filas, 1 columna de gráficos

# Gráfico de líneas
system('cls')
axs[0].plot(x, y, label="Seno de x", color='blue')
axs[0].set_title("Gráfico de Líneas")
axs[0].set_xlabel("x")
axs[0].set_ylabel("sin(x)")
axs[0].legend()

# Histograma
axs[1].hist(data, bins=30, color='green', alpha=0.7)
axs[1].set_title("Histograma de Datos Aleatorios")
axs[1].set_xlabel("Valor")
axs[1].set_ylabel("Frecuencia")

# Ajustar el espaciado entre los subplots
plt.tight_layout()

# Mostrar los gráficos
plt.show()
