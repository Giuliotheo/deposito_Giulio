
# Prende in input un numero
numero = int(input("Inserisci un numero: "))

# Controlla se è pari o dispari
if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")
    
    
    
    
#esercizio 3

# Chiediamo all'utente di inserire numeri separati da virgole
numeri_input = input("Inserisci una lista di numeri separati da virgole: ")

# Convertiamo la stringa in una vera lista di numeri interi
lista = numeri_input.split(",")  # ["2", "5", "7"]
numeri = [int(x) for x in lista]  # [2, 5, 7]

# Ciclo for per calcolare il quadrato di ciascun numero
for numero in numeri:
    quadrato = numero ** 2
    print(f"Il quadrato di {numero} è {quadrato}")
    
    
    
    #esercizio 4
    
    # Input dell'utente
input_utente = input("Inserisci una lista di numeri separati da virgole: ")

# Creiamo la lista solo se l'utente ha scritto qualcosa
if input_utente.strip() == "":
    numeri = []
else:
    numeri = [int(x) for x in input_utente.split(",")]

# Punto 3: Controllo con if
if len(numeri) == 0:
    print("Lista vuota")
else:
    # Punto 1: Trova il numero massimo con ciclo for
    massimo = numeri[0]
    for numero in numeri:
        if numero > massimo:
            massimo = numero

    # Punto 2: Conta gli elementi con ciclo while
    conteggio = 0
    i = 0
    while i < len(numeri):
        conteggio += 1
        i += 1

    # Stampa i risultati
    print("Numero massimo:", massimo)
    print("Numero di elementi nella lista:", conteggio)