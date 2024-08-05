import pandas as pd

# Nome do arquivo CSV a ser lido
csv_file = 'dados.csv'

# Ler o arquivo CSV
df = pd.read_csv(csv_file, sep=',', engine='python', encoding='utf-8')

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
