import matplotlib.pyplot as plt
import numpy as np

mes = np.arange(12) + 1 # meses de 1 a 12

# quantidades de produtos vendidos por mês
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

# Gráfico 1 - Total de produtos Vendidos por mês - Linha
print("# Gráfico 1 - Total de produtos Vendidos por mês - Linha")
fig, ax = plt.subplots()
y = np.array(creme_facial+limpeza_facial+pasta_dentaria+sabonete+shampoo+hidratante)
ax.set_xlabel('Mês')
ax.set_ylabel('Qtd Vendas')
ax.set_title("Produtos Vendidos por Mês")
ax.plot(mes,y)
fig.set_size_inches(10, 5.4)
ax.set_xticks(mes)
ax.set_xticklabels(mes)
plt.show()

# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
print("\n\n# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha")
fig, ax = plt.subplots()
ax.plot(mes,creme_facial, label='Creme Facial')
ax.plot(mes,limpeza_facial, label='Limpeza Facial')
ax.plot(mes,pasta_dentaria, label='Pasta Dentária')
ax.plot(mes,sabonete, label='Sabonete')
ax.plot(mes,shampoo, label='Shampoo')
ax.plot(mes,hidratante, label='Hidratante')
ax.set_xlabel("Mês")
ax.set_ylabel("Qtd Vendas")
ax.set_title("Complexidade algorítmica")
ax.legend()
fig.set_size_inches(10, 5.4)
ax.set_xticks(mes)
ax.set_xticklabels(mes)
plt.show()

# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras
print("\n\n# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras")
fig, ax = plt.subplots()
wdth = 0.40
ax.bar(mes-wdth/2,creme_facial,wdth, label="Creme Facial")
ax.bar(mes+wdth/2,limpeza_facial,wdth, label="Limpeza Facial")
fig.set_size_inches(10, 5.4)
ax.set_xticks(mes)
ax.legend()
ax.set_xticklabels(mes)
plt.show()

# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)
print("\n\n# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...")
fig, ax = plt.subplots()
ax.hist(y, edgecolor="white")
ax.set_xlabel('Valores')
ax.set_ylabel('Ocorrências')
ax.set_title('Gaussiana')
plt.show()

# Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto
print("\n\n# Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto")
y = np.array([np.sum(creme_facial), np.sum(limpeza_facial), np.sum(pasta_dentaria), np.sum(sabonete), np.sum(shampoo), np.sum(hidratante)])
text = ["Creme Facial", "Limpeza Facial", "Pasta Dentária", "Sabonete", "Shampoo", "Hidratante"]
fig, ax = plt.subplots()
plt.pie(y, labels = text, shadow=True)
fig.set_size_inches(10, 5.4)
plt.show()