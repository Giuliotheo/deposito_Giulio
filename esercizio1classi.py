
# esercizio 1 classi

#classe Punto
class Punto():
    
    def __init__(self, x ,y ):
        self.x = x
        self.y = y
    
    def muovi_punti(self, newX, newY):
        if newX>0 and newY>0:
            self.x = newX
            self.y = newY
            print("la distanza dal origine x ora e ", self.x)
            print("la distanza dal origine xy ora e ", self.y)
        else:
            print("il valore è negativo o 0")
#menu per la gestione dei Punti cartesiani           
while True:
    scelta = ("vuoi creare il punto?")
    if scelta.lower == "si":
        x_ins = input("inserisci la coordinata x")
        y_ins = input("inserisci la coordinata y")
        Punto_mio = Punto(x_ins, y_ins)
        
    scelta = ("vuoi modificare le coordinate?")
    if scelta.lower == "si":
        x_ins = input("inserisci la coordinata x")
        y_ins = input("inserisci la coordinata y")
        Punto_mio.muovi_punti(x_ins,y_ins)
    
    scelta_ciclo = ("vuoi ripetere?")
    if scelta_ciclo.lower == "si":
        continue
    else:
        break
    