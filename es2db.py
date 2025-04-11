
import sqlite3
import random

# 1. Crea un database chiamato libreria.db
conn = sqlite3.connect("libreria.db")
cur = conn.cursor()

# 2. Crea una tabella chiamata libri con id, titolo e autore
cur.execute("""
    CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT,
        autore TEXT
    )
""")

# 3. Inserisce 3 libri a scelta
libri = [
    ("Harry Potter", "J.K. Rowling"),
    ("1984", "George Orwell"),
    ("Il Piccolo Principe", "Antoine de Saint-Exupéry")
]
cur.executemany("INSERT INTO libri (titolo, autore) VALUES (?, ?)", libri)

# 4. Stampa tutti i libri (id, titolo, autore)
print("Lista dei libri:")
cur.execute("SELECT id, titolo, autore FROM libri")
for libro in cur.fetchall():
    print(libro)

# 5. Aggiunge una colonna VENDITE con numeri casuali
try:
    cur.execute("ALTER TABLE libri ADD COLUMN vendite INTEGER")
except sqlite3.OperationalError:
    pass  # La colonna esiste già

# Aggiorna ogni libro con un numero di vendite random
cur.execute("SELECT id FROM libri")
for (book_id,) in cur.fetchall():
    vendite = random.randint(0, 1000)
    cur.execute("UPDATE libri SET vendite = ? WHERE id = ?", (vendite, book_id))

# Stampa i dati completi con vendite
print("Lista aggiornata con vendite:")
cur.execute("SELECT * FROM libri")
for libro in cur.fetchall():
    print(libro)

# Chiude la connessione
conn.commit()
conn.close()