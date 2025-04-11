import sqlite3

# 1. Connessione al database (lo crea se non esiste)
conn = sqlite3.connect("test.db")
cur = conn.cursor()

# 2. Crea la tabella solo se non esiste
cur.execute('''
    CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT
    )
''')

# 3. Inserisce dati nella tabella (solo se vuota)
libri = [("Harry Potter",), ("1984",), ("Il Piccolo Principe",)]
cur.executemany("INSERT INTO libri (titolo) VALUES (?)", libri)

# 4. Salva le modifiche
conn.commit()

# 5. Legge una riga
cur.execute("SELECT * FROM libri")
riga = cur.fetchone()
print(riga)

# 6. Chiude la connessione
conn.close()


# metodo executemany
conn = sqlite3.connect("test.db")
cur = conn.cursor()

libri = [("Harry Potter",), ("1984",), ("Il Piccolo Principe",)]
cur.executemany("INSERT INTO libri (titolo) VALUES (?)", libri)

conn.commit()
conn.close()


# Metodo fetchone
conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("SELECT * FROM libri")
riga = cur.fetchone()

print(riga)  # Mostra solo la prima riga




conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("SELECT * FROM libri")
# Recupera tutte le righe del risultato e le memorizza in una lista.
tutte_le_righe = cur.fetchall()
# Scorre ogni riga dei risultati.
for riga in tutte_le_righe:
    print(riga)




# Metodo commit
conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("INSERT INTO libri (titolo) VALUES (?)", ("Il Nome della Rosa",))
conn.commit()  # Salva la modifica

conn.close()









