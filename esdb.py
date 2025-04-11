

import sqlite3  

# Chiede all’utente se creare un nuovo database
risposta_Db = input("Vuoi inserire un nuovo DB scolastico? SI/NO ").upper()

if risposta_Db == "SI":
    nome_DB = input("Scrivi il nome del file del DB (es. scuola.db): ")
    
    # Crea la connessione e il cursore
    conn = sqlite3.connect(nome_DB)
    cur = conn.cursor()
    print(f"Hai creato (o aperto) il database '{nome_DB}'")

    # Crea la tabella 'studenti'
    cur.execute('''
        CREATE TABLE IF NOT EXISTS studenti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    ''')

    # Inserimento studenti con un ciclo
    while True:
        scelta = input("Vuoi inserire un nuovo studente? SI/NO ").upper()
        if scelta == "SI":
            nome = input("Inserisci il nome dello studente: ")
            cur.execute("INSERT INTO studenti (nome) VALUES (?)", (nome,))
            conn.commit()
            print("Hai aggiunto uno studente.")
        else:
            break

    # Mostra l'elenco degli studenti
    print("Lista degli studenti:")
    cur.execute("SELECT * FROM studenti")
    righe = cur.fetchall()
    for riga in righe:
        print(riga)

    conn.close()
    print("Connessione chiusa.")

else:
    print("Nessun database creato.")