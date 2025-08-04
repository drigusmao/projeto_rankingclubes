# Projeto: Ranking de Clubes Internacionais

### Este projeto em Python realiza a extração e análise de dados de clubes de futebol campeões internacionais diretamente da Wikipedia.

### Conceitos Aplicados: 

- Leitura de tabelas HTML diretamente de páginas da web com pd.read_html()
- Seleção e limpeza de colunas (.columns.str.strip())
- Conversão de tipos de dados (pd.to_numeric)
- Ordenação de dados (.sort_values)
- Filtragem com expressões booleanas (df[df['coluna'] < valor])
- Seleção de colunas específicas ([['col1', 'col2']])
- Visualização de dados:
- Gráfico de barras (plt.bar)
- Ajuste de rótulos e rotação (plt.xticks)
- Salvamento de gráfico como imagem (plt.savefig)
- Exportação de gráfico para arquivo PNG

### Tecnologias Utilizadas:

- Python 3.x
- Pandas → manipulação e análise de dados
- Matplotlib → visualização gráfica
