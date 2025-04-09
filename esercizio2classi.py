
# esercizio 2
# definizione classe
class Libro:
# costruttore che riceve 3 parametri dall'utente
    def __init__(self, titolo, autore, pagine):
# attributo dell'oggetto es: (libro1).
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
# metodo della classe
    def descrizione(self):
# Restituzione della frase formattata con f-string.
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha {self.pagine} pagine."

# Esempio d'uso:
libro1 = Libro("A un passo dal declino", "Giulio Theodoli", 350)
print(libro1.descrizione())