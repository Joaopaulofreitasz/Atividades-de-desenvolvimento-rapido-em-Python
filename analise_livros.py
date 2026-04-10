import pandas as pd

# lendo o arquivo csv (separado por ;)
df = pd.read_csv("livros.csv", sep=";")

# olhando as primeiras linhas pra entender os dados
print("Primeiras 5 linhas:")
print(df.head())

# verificando estrutura e tipos das colunas
print("\nInformações gerais:")
print(df.info())

# estatísticas básicas das colunas numéricas
print("\nEstatísticas descritivas:")
print(df.describe())

# checando valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# filtrando livros com 0 páginas (provavelmente erro)
livros_zero = df[df["paginas"] == 0]
print("\nLivros com 0 páginas:")
print(livros_zero)
print("Quantidade:", len(livros_zero))

# vendo quantos livros foram publicados por ano
print("\nQuantidade de livros por ano:")
livros_por_ano = df["ano"].value_counts().sort_index()
print(livros_por_ano)

# criando uma classificação simples por tamanho do livro
df["faixa_paginas"] = df["paginas"].apply(
    lambda x: "Curto" if x < 150 else ("Médio" if x <= 350 else "Longo")
)

print("\nColuna faixa_paginas criada:")
print(df[["paginas", "faixa_paginas"]].head())

# removendo registros com páginas igual a 0
df_limpo = df[df["paginas"] > 0].copy()

# calculando quantos foram removidos
removidos = len(df) - len(df_limpo)
print("\nRegistros removidos:", removidos)

# preenchendo valores faltantes de ano com a mediana
mediana_ano = df_limpo["ano"].median()
df_limpo["ano"] = df_limpo["ano"].fillna(mediana_ano)

# convertendo pra inteiro
df_limpo["ano"] = df_limpo["ano"].astype(int)

print("\nNulos em 'ano':")
print(df_limpo["ano"].isnull().sum())

# criando coluna de década (ex: 2019 vira 2010)
df_limpo["decada"] = (df_limpo["ano"] // 10) * 10

print("\nColuna década:")
print(df_limpo[["ano", "decada"]].head())

# média de páginas por década
media_paginas_decada = (
    df_limpo.groupby("decada")["paginas"]
    .mean()
    .sort_index()
)

print("\nMédia de páginas por década:")
print(media_paginas_decada)

# autores com mais livros no dataset
top_autores = df_limpo["autor"].value_counts().head(10)

print("\nTop 10 autores:")
print(top_autores)

# distribuição do tamanho dos livros depois de 2010
distribuicao = df_limpo[df_limpo["ano"] > 2010]["faixa_paginas"].value_counts()

print("\nDistribuição após 2010:")
print(distribuicao)

# exportando o resultado final para excel
df_limpo.to_excel("livros_analisados.xlsx", index=False)

print("\nArquivo exportado com sucesso!")