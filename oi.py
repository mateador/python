"""
Visualização de dados em Python
"""

import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]
titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Título
plt.title(titulo)

#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y)
plt.show()
