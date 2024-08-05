import pandas as pd

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
