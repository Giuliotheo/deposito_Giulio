#esercizio 1 cicli
for i in range(2, 8):
    print(i)


#inserimento numero e conto alla rovescia

ripeti = "sì"

while ripeti.lower() == "sì":
    numero = int(input("Inserisci un numero intero: "))

    print("Conto alla rovescia:")
    for i in range(numero, -1, -1,):
        print(i)

    ripeti = input("Vuoi ripetere? (sì/no): ")

print("Programma terminato. Ciao!")




#esercizio 2, controllo numero se è primo,pari,dispari o no


primi = []

while len(primi) < 5:
    numero = int(input("Inserisci un numero: "))

    # Verifica se è primo
    if numero > 1:
        è_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                è_primo = False
                break
    else:
        è_primo = False

    # Stampiamo i risultati
    if è_primo:
        print(" Il numero è primo.")
        primi.append(numero)
    else:
        print(" Il numero non è primo.")

    # Controllo pari/dispari
    if numero % 2 == 0:
        print("È un numero pari.")
    else:
        print(" È un numero dispari.")

print("Hai trovato 5 numeri primi:", primi)





# lista per salvare i  numeri pari trovati
numeri_pari = []

# ciclo finchè non abbiamo trovato 5 numeri pari
while len(numeri_pari) < 5:
    numero = int(input("inserisci un numero: "))
    
    if numero % 2 == 0:
        print("il numero è paro")
        numeri_pari.append(numero)
    else:
        print("il numero non è pari")

# alla fine stampa i numeri pari raccolti
print("hai inserito 5 numeri pari:", numeri_pari)

risposta = True
while risposta:
    
    risposta = input("vuoi continuare?")
    if risposta == "no":
        risposta = False