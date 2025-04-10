# ESERCIZIO
import pandas as pd
import numpy as np

# Lista di nomi e città da usare
nomi = ['Alice', 'Bob', 'Carla', 'Daniele', 'Elisa', 'Franco', 'Giulia', 'Luca', 'Marta', 'Paolo']
città = ['Roma', 'Milano', 'Napoli']

# Costruzione dati casuali
np.random.seed(0)  # Per risultati ripetibili
dati = {
    'Nome': np.random.choice(nomi, 20),
    'Età': np.random.randint(15, 80, 20),
    'Città': np.random.choice(città, 20),
    'Salario': np.random.randint(1000, 5000, 20)
}

df = pd.DataFrame(dati)

df.loc[5, 'Età'] = np.nan
df.loc[10, 'Salario'] = np.nan
# Visualizza le prime e ultime 5 righe
print("Prime 5 righe:\n", df.head())
print("\nUltime 5 righe:\n", df.tail())

# Visualizza il tipo di dati di ogni colonna
print("\nTipi di dati:\n", df.dtypes)

# Calcola statistiche di base
print("\nStatistiche descrittive:\n", df.describe())

# Rimozione eventuali duplicati
df = df.drop_duplicates()

# Gestione dei valori mancanti: sostituzione con la mediana della colonna
df['Età'].fillna(df['Età'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)

# Aggiunta della colonna “Categoria Età”
def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df['Categoria Età'] = df['Età'].apply(categoria_eta)

# Salvataggio in un file CSV
df.to_csv("df_pulito.csv", index=False)
print("\nFile salvato come 'df_pulito.csv'")


