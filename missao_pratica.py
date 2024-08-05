import pandas as pd

# Nome do arquivo CSV
csv_file = 'dados1.csv'

# Ler o arquivo CSV
df = pd.read_csv(csv_file, sep=';', engine='python', encoding='utf-8')

# Verificar importação
print("Informações Gerais do DataFrame:")
print(df.info())

print("\nPrimeiras 5 Linhas:")
print(df.head())

print("\nÚltimas 5 Linhas:")
print(df.tail())

# Criar uma cópia dos dados
df_copy = df.copy()

# Substituir valores nulos na coluna 'Calories' por 0
df_copy['Calories'].fillna(0, inplace=True)
print("\nDataFrame após substituir valores nulos na coluna 'Calories':")
print(df_copy)

# Substituir valores nulos na coluna 'Date' por '1900/01/01'
df_copy['Date'].fillna('1900/01/01', inplace=True)
print("\nDataFrame após substituir valores nulos na coluna 'Date':")
print(df_copy)

# Corrigir formato específico de datas
df_copy['Date'] = df_copy['Date'].str.strip("'")
df_copy['Date'] = df_copy['Date'].astype(str).replace({'20201226': '2020/12/26'})
df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%Y/%m/%d', errors='coerce')
print("\nDataFrame após corrigir datas no formato '20201226':")
print(df_copy)

# Transformar a coluna 'Date' em datetime
df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='%Y/%m/%d', errors='coerce')
print("\nDataFrame após transformar a coluna 'Date' em datetime:")
print(df_copy)

# Transformar na coluna Date o valor ‘1900/01/01’ por ‘NaN’
df_copy['Date'].replace(pd.Timestamp('1900-01-01'), pd.NaT, inplace=True)
print(df_copy)

# Remover registros com valores nulos na coluna 'Date'
df_clean = df_copy.dropna(subset=['Date'])
print("\nDataFrame após remover registros com valores nulos na coluna 'Date':")
print(df_clean)
