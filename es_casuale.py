# esercizio 1

import random  # Per generare numeri casuali

def indovina_il_numero():
    numero_segreto = random.randint(1, 100)
    print(" Ho scelto un numero tra 1 e 100. Riuscirai a indovinarlo?")
    tentativi = 0

    while True:
        risposta = input("Inserisci un numero oppure scrivi 'esci' per terminare: ")

        if risposta.lower() == "esci":
            print(" Hai deciso di uscire dal gioco. Il numero era:", numero_segreto)
            break

        if risposta.isdigit():
            numero = int(risposta)
            tentativi += 1

            if numero < numero_segreto:
                print(" Troppo basso! Riprova.")
            elif numero > numero_segreto:
                print(" Troppo alto! Riprova.")
            else:
                print(f" Complimenti! Hai indovinato in {tentativi} tentativi!")
                break
        else:
            print(" Inserisci un numero valido o scrivi 'esci'.")
            
# Avvio del gioco
indovina_il_numero()