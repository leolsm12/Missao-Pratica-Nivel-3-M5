import pandas as pd


# Nome do arquivo CSV
csv_file = 'dados.csv'

# Nome do arquivo CSV para salvar o subconjunto
subconjunto_csv_file = 'subconjunto_dados.csv'

# Ler o arquivo CSV
df_csv = pd.read_csv(csv_file, sep=',', engine='python', encoding='utf-8')

# Exibir os dados do arquivo CSV
print("Dados completos:")
print(df_csv)

# Microatividade 2: Criar um subconjunto de dados

# Crie uma nova variável com um subconjunto de dados contendo apenas 3 colunas
subconjunto = df_csv[['InvoiceNo', 'StockCode', 'Description']]

# Salvar o subconjunto em um novo arquivo CSV
subconjunto.to_csv(subconjunto_csv_file, index=False)

# Exibir o subconjunto de dados
print("\nSubconjunto de dados:")
print(subconjunto)