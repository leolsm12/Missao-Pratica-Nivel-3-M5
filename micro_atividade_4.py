import pandas as pd

csv_file = 'dados.csv'

# Ler o arquivo CSV
df_csv = pd.read_csv(csv_file, sep=',', engine='python', encoding='utf-8')

# Imprimir as 10 primeiras linhas
print("10 Primeiras Linhas:")
print(df_csv.head(10))

# Imprimir as 10 últimas linhas
print("10 Últimas Linhas:")
print(df_csv.tail(10))