
# dichiaro la classe
class Automobile:
# attributo di classe
    numero_di_ruote = 4
# metodo costruttore
    def __init__(self, marca, modello):
#attributo di istanza
        self.marca = marca
        self.modello = modello
# metodo di istanza
    def stampa_info(self):
        
        print("l'automobile è una", self.marca, self.modello)
        





class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def saluta(self):
        print(f"Ciao! Mi chiamo {self.nome} e ho {self.età} anni.")

# Creazione oggetto
p = Persona("Giulio", 30)

# Chiamata al metodo
p.saluta()




# esempio metodo statico
class Calcolatrice:
    
    @staticmethod
    def somma(a, b):
        return a + b
    
# uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)

print(risultato)
# Output: 8









class Contatore:
    numero_istanze = 0  # Attributo di classe

    def __init__(self):
        Contatore.numero_istanze += 1

    @classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state create {cls.numero_istanze} istanze.")

# Creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
# Output: Sono state create 2 istanze.



