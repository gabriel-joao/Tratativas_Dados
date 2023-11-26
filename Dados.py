import os
import pandas as pd
import plotly.express as px

pasta_vendas = "C:\\Users\\souza\\PycharmProjects\\TestPyCharm\\Pasta\\Vendas"

list_arquivos = os.listdir(pasta_vendas)
table_total = pd.DataFrame()

for arquivo in list_arquivos:
    if "Vendas" in arquivo and arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(pasta_vendas, arquivo)
        tabela = pd.read_csv(caminho_arquivo)
        table_total = pd.concat([table_total, tabela], ignore_index=True)

table_produtos = table_total.groupby("Produto").sum()[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(table_produtos)

table_total["Faturamento"] = table_total["Quantidade Vendida"] * table_total["Preco Unitario"]
table_faturamento = table_total.groupby("Produto").sum()[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(table_faturamento)

table_lojas = table_total.groupby("Loja").sum()[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
print(table_lojas)

grafico_produtos = px.bar(table_produtos, x=table_produtos.index, y="Quantidade Vendida")
grafico_faturamento = px.bar(table_faturamento, x=table_faturamento.index, y="Faturamento")
grafico_lojas = px.bar(table_lojas, x=table_lojas.index, y="Faturamento")

grafico_produtos.show()
grafico_faturamento.show()
grafico_lojas.show()
