Nome - João Paulo de Freitas Costa
Matrícula - 202404000095

# Análise de Livros com Pandas

Este projeto consiste na análise de um dataset com aproximadamente 12.000 livros, utilizando a biblioteca Pandas em Python. O objetivo é explorar, limpar e extrair informações relevantes a partir dos dados.

## Dataset

O arquivo utilizado (`livros.csv`) possui as seguintes colunas:

- titulo: título do livro  
- autor: nome do autor  
- isbn: código identificador do livro  
- paginas: número de páginas  
- ano: ano de publicação  

## Etapas do Projeto

### 1. Exploração dos dados
- Visualização das primeiras linhas
- Verificação de tipos de dados
- Estatísticas descritivas
- Identificação de valores nulos
- Análise de registros inconsistentes (ex: livros com 0 páginas)
- Quantidade de livros publicados por ano

### 2. Limpeza e transformação
- Criação da coluna `faixa_paginas` (Curto, Médio, Longo)
- Remoção de registros inválidos (páginas igual a 0)
- Tratamento de valores nulos na coluna `ano`
- Criação da coluna `decada`

### 3. Análise dos dados
- Média de páginas por década
- Top 10 autores com mais livros
- Distribuição do tamanho dos livros após 2010

### 4. Exportação
- Geração de um novo arquivo `livros_analisados.xlsx` com os dados tratados

## Tecnologias utilizadas

- Python
- Pandas

## Como executar

1. Clone o repositório: git clone <https://github.com/Joaopaulofreitasz/Atividades-de-desenvolvimento-rapido-em-Python/new/main?filename=README.md>
2. Acesse a pasta do projeto: cd <atividade aula 03>
3. Instale as dependências (se necessário): pip install pandas openpyxl
4. Execute o script: python analise_livros.py
