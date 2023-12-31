"""
Visualização de dados em Python
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]

titulo = "Scatterplt"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Título
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.legend()

plt.savefig("figura1.png", dpi=300)

#plt.show()
