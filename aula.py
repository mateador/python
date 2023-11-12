# gráfico

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color="k", linestyle="--")
plt.scatter(x, y, color="k")

plt.title("Crescimento da população brasileira")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")


plt.show()
#plt.savefig("popucacao.png", dpi=300)