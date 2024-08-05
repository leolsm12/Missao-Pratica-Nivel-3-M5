import pandas as pd

# Nome do arquivo CSV a ser salvo
csv_file = 'dados.csv'

# Ler o arquivo CSV
df_csv = pd.read_csv(csv_file, sep=',', engine='python', encoding='utf-8')

# Configurar o número máximo de linhas a serem exibidas
pd.set_option('display.max_rows', 9999)

# Exibir os dados do arquivo CSV usando to_string()
print("Dados completos:")
print(df_csv.to_string())
