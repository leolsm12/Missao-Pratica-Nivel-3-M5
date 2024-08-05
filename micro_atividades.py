import pandas as pd
# Microatividade 2:Descrever como ler um arquivo CSV usando a biblioteca Pandas (Python)
# Nome do arquivo XLSX a ser lido
xlsx_file = 'dados.xlsx'

# Nome do arquivo CSV a ser salvo
csv_file = 'dados.csv'

# Ler o arquivo XLSX
df = pd.read_excel(xlsx_file)

# Salvar como CSV
df.to_csv(csv_file, index=False)

# Ler o arquivo CSV
df_csv = pd.read_csv(csv_file, sep=',', engine='python', encoding='utf-8')

# Exibir os dados
print(df_csv)

# Microatividade 2: Descrever como criar um subconjunto de dados a partir
# de um conjunto existente usando a biblioteca Pandas (Python)

# Nome do arquivo CSV para salvar o subconjunto
subconjunto_csv_file = 'subconjunto_dados.csv'

# Crie uma nova variável com um subconjunto de dados contendo apenas 3 colunas
subconjunto = df_csv[['InvoiceNo', 'StockCode', 'Description']]

# Salvar o subconjunto em um novo arquivo CSV
subconjunto.to_csv(subconjunto_csv_file, index=False)

# Exibir o subconjunto de dados
print("\nSubconjunto de dados:")
print(subconjunto)

# Microatividade 3: Descrever como configurar o número máximo de linhas a
# serem exibidas na visualização de um conjunto de dados usando a biblioteca
# Pandas (Python)

# Configurar o número máximo de linhas a serem exibidas
pd.set_option('display.max_rows', 9999)

# Exibir os dados do arquivo CSV usando to_string()
print("Dados completos:")
print(df_csv.to_string())

# Microatividade 4: Descrever como exibir as primeiras e últimas “N” linhas de um
# conjunto de dados usando a biblioteca Pandas (Python)

# Imprimir as 10 primeiras linhas
print("10 Primeiras Linhas:")
print(df_csv.head(10))

# Imprimir as 10 últimas linhas
print("10 Últimas Linhas:")
print(df_csv.tail(10))

# Microatividade 3:  Descrever como exibir informações gerais sobre as colunas, linhas
# e dados de um conjunto de dados usando a biblioteca Pandas (Python)

# Exibir informações gerais sobre o DataFrame
print("Informações Gerais do DataFrame:")
print(df.info())

# Total de linhas
total_linhas = df.shape[0]
print(f"\nTotal de Linhas: {total_linhas}")

# Total de colunas
total_colunas = df.shape[1]
print(f"Total de Colunas: {total_colunas}")

# Quantidade de dados nulos em cada coluna
dados_nulos = df.isnull().sum()
print("\nQuantidade de Dados Nulos por Coluna:")
print(dados_nulos)

# Tipo de dado de cada coluna
tipos_dados = df.dtypes
print("\nTipo de Dado de Cada Coluna:")
print(tipos_dados)

# Quantidade de memória utilizada
memoria_utilizada = df.memory_usage(deep=True).sum()
print(f"\nQuantidade de Memória Utilizada (bytes): {memoria_utilizada}")

