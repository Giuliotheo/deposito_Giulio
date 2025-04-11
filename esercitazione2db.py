
import sqlite3

# Connessione al database (o creazione se non esiste)
conn = sqlite3.connect("miodatabase.db")
cur = conn.cursor()

# Creazione tabella
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

# Commit delle modifiche
conn.commit()

# Chiusura connessione SOLO ALLA FINE
conn.close()

import sqlite3

# Connessione al database
conn = sqlite3.connect("miofile.db")
cur = conn.cursor()

# Creazione tabella (opzionale)
cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')


conn.commit()  # Importante: salva le modifiche
cur.execute("INSERT INTO utenti (nome) VALUES (?)", ("Mirko",))

#lettura dei dati
cur.execute("SELECT * FROM utenti")
righe = cur.fetchall()
for r in righe:
    print(r)
    
    
# modifica dei dati
    cur.execute("UPDATE utenti SET nome = ? WHERE id = ?", ("Luigi", 1))
conn.commit()


# eliminazione dei dati
cur.execute("DELETE FROM utenti WHERE id = ?", (1,))
conn.commit()

    
    
