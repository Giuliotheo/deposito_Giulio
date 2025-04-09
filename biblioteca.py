
# Esercizio
# Classe che rappresenta un libro
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        return f" Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha {self.pagine} pagine."


# Classe che gestisce una raccolta di libri
class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self):
        titolo = input("Titolo del libro: ")
        autore = input("Autore del libro: ")
        pagine = int(input("Numero di pagine: "))
        nuovo_libro = Libro(titolo, autore, pagine)
        self.libri.append(nuovo_libro)
        print(" Libro aggiunto!")

    def stampa_libri(self):
        print(" Libri in biblioteca:")
        if not self.libri:
            print("Nessun libro presente.")
        else:
            for libro in self.libri:
                print(libro.descrizione())

    def cerca_libro(self, titolo_da_cercare):
        trovato = False
        for libro in self.libri:
            if libro.titolo.lower() == titolo_da_cercare.lower():
                print(" Libro trovato:")
                print(libro.descrizione())
                trovato = True
                break
        if not trovato:
            print(" Libro non trovato.")


# Programma principale
mia_biblioteca = Biblioteca()

#  Aggiunta automatica del libro di Giulio Theodoli
libro_giulio = Libro("A un passo dal declino", "Giulio Theodoli", 350)
mia_biblioteca.libri.append(libro_giulio)
print(" Libro 'A un passo dal declino' di Giulio Theodoli aggiunto automaticamente.")

# Menu interattivo
while True:
    scelta = input("\nVuoi aggiungere un libro, cercare o uscire? (aggiungi/cerca/esci): ")

    if scelta.lower() == "aggiungi":
        mia_biblioteca.aggiungi_libro()

    elif scelta.lower() == "cerca":
        titolo_cercato = input("Inserisci il titolo del libro da cercare: ")
        mia_biblioteca.cerca_libro(titolo_cercato)

    elif scelta.lower() == "esci":
        break

    else:
        print("Comando non valido. Scrivi 'aggiungi', 'cerca' o 'esci'.")

# Stampa tutti i libri presenti
mia_biblioteca.stampa_libri()