# Importa a biblioteca pandas que vamos utilizar para a analise
import pandas as pd

# Escolher um link(site) que contenha a tabela para conversão no Python utilizando pandas
# Clique com o botão direito do mouse na página onde se encontra a tabela que queira ler com pandas e depois em Salvar Como (pagina completa ou somente HTML) com o nome escolhido e ao final ".html"

# Enviar para o VSCode o URL da página da Wikipedia com a lista de clubes campeões internacionais
url = 'https://pt.wikipedia.org/wiki/Lista_de_clubes_campe%C3%B5es_internacionais_de_futebol'

# Lê todas as tabelas da página escolhida 
tabelas = pd.read_html(url)

# Verifica quantas tabelas foram encontradas
print(f'Total de tabelas encontradas: {len(tabelas)}')

# Seleciona a tabela de interesse
clubes = tabelas[1]

# Redefine o DataFrame(estrutura de dados bidimensional que organiza informações em linhas e colunas, similar a uma planilha ou uma tabela de banco de dados) pulando linhas até atingir o cabeçalho correto
clubes = pd.read_html(url, header=0)[1]

# Limpa colunas (remove espaços)
clubes.columns = clubes.columns.str.strip()

# Converte Títulos para numérico
clubes['Títulos'] = pd.to_numeric(clubes['Títulos'], errors='coerce')

# Ordena e exibe os top 10 clubes com mais títulos
top10 = clubes.sort_values(by='Títulos', ascending=False).head(10)
print("\nTop 10 clubes com mais títulos internacionais")
print(top10[['Clube', 'Títulos']])

# Filtra clubes com menos de 10 títulos
menos_de_10 = clubes[clubes['Títulos'] < 10]
print("\nClubes com menos de 10 títulos internacionais:")
print(menos_de_10[['Clube', 'Títulos']])













