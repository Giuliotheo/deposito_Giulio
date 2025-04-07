
numeroconlavirgola = 3.14

#tipi numerici
intero = int(input("inserisci un intero"))
virgola = float(input("inserisci un numero con la virgola"))


#tipi semantici
stringa = input("inserisci una parola")
print(stringa[0])
print(stringa.lower())




s = "Ciao, mondo!"
print(len(s))
print(s.upper())
print(s.split(','))
print(s.replace('mondo', 'universo'))




#valori booleani
x= False
y= True
numero1 = 5
numero2 = 11
print(5>11)
print(13<50)

#liste

lista_dati = [1,4,2,3,0]
lista_dati2 = [1,"mirko", True]
lista_dati3 = []

print(lista_dati)
print(lista_dati[2])
print(lista_dati2[1])

print(lista_dati.sort())


inserimento = int(input("inserisci un numero"))
lista_dati3.append(inserimento)
inserimento = int(input("inserisci un numero"))
lista_dati3.append(inserimento)

print(lista_dati3)


#controllo del flusso

numero = 10
if numero > 20:
    print("il numero è positivo")
else:
    print("Blocco Else")
