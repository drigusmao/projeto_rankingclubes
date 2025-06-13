# Importa bibliotecas necessárias
import pandas as pd  # Usada para análise e manipulação de dados em tabelas (DataFrames)
import matplotlib.pyplot as plt  # Usada para criar gráficos e visualizações de dados

# Define o link da página da Wikipedia com a lista de clubes campeões internacionais
url = 'https://pt.wikipedia.org/wiki/Lista_de_clubes_campe%C3%B5es_internacionais_de_futebol'

# Lê todas as tabelas HTML da página e armazena em uma lista
tabelas = pd.read_html(url)

# Seleciona a tabela correta (índice 1) com os dados dos clubes e títulos
clubes = pd.read_html(url, header=0)[1]

# Remove espaços em branco dos nomes das colunas
clubes.columns = clubes.columns.str.strip()

# Converte a coluna 'Títulos' para tipo numérico (ignora erros como strings ou valores ausentes)
clubes['Títulos'] = pd.to_numeric(clubes['Títulos'], errors='coerce')

# Exibe as 10 primeiras linhas da tabela como visualização inicial
print("\nPrimeiras 10 linhas da tabela:")
print(clubes.head(10))

# Ordena os clubes por número de títulos e seleciona os 10 primeiros
top10 = clubes.sort_values(by='Títulos', ascending=False).head(10)
print("\nTop 10 clubes com mais títulos internacionais:")
print(top10[['Clube', 'Títulos']])

# Cria um gráfico de barras com os 10 clubes mais vitoriosos
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.bar(top10['Clube'], top10['Títulos'], color='skyblue')  # Cria as barras com cor azul-claro
plt.xticks(rotation=45, ha='right')  # Rotaciona os nomes dos clubes para melhor leitura
plt.title('Top 10 Clubes com Mais Títulos Internacionais')  # Título do gráfico
plt.xlabel('Clube')  # Legenda do eixo X
plt.ylabel('Número de Títulos')  # Legenda do eixo Y
plt.tight_layout()  # Ajusta espaçamento automático
plt.savefig('grafico_top10.png')  # Salva o gráfico como imagem PNG
plt.show()  # Exibe o gráfico

# Filtra clubes com menos de 10 títulos
menos_de_10 = clubes[clubes['Títulos'] < 10]
print("\nClubes com menos de 10 títulos internacionais:")
print(menos_de_10[['Clube', 'Títulos']])

