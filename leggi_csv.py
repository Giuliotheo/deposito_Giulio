import pandas as pd
# codice per leggere il file CSV

# Percorso del file CSV (se è nella stessa cartella va bene così)
file_path = "df_pulito.csv"

# Caricamento del file nel DataFrame
df = pd.read_csv(file_path)

# Stampa delle prime 5 righe
print("Prime righe del CSV:")
print(df.head())