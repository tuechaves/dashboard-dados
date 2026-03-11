import pandas as pd
import matplotlib.pyplot as plt

# ler arquivo CSV
df = pd.read_csv("data/vendas.csv")

# mostrar dados
print(df)

# análise
vendas_produto = df.groupby("Produto")["Vendas"].sum()

print("\nVendas por produto:")
print(vendas_produto)

# gráfico
vendas_produto.plot(kind="bar")

plt.title("Vendas por Produto")
plt.xlabel("Produto")
plt.ylabel("Total de vendas")

plt.show()