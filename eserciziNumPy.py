

import numpy as np
# ESERCIZIO 1

# Crea un array di 12 numeri equidistanti tra 0 e 1
arr_linspace = np.linspace(0, 1, 12)
print("Array linspace:")
print(arr_linspace)

# Cambia la forma dell'array in una matrice 3x4
mat_linspace = arr_linspace.reshape(3, 4)
print("Matrice 3x4 da linspace:")
print(mat_linspace)

# Genera una matrice 3x4 di numeri casuali tra 0 e 1
mat_random = np.random.rand(3, 4)
print("Matrice casuale 3x4:")
print(mat_random)

# Calcola e stampa la somma degli elementi di entrambe le matrici
sum_linspace = np.sum(mat_linspace)
sum_random = np.sum(mat_random)

print("Somma elementi linspace:", sum_linspace)
print("Somma elementi matrice casuale:", sum_random)


# con extra

# Classe per gestire l'esercizio
class EsercizioArray:

    def __init__(self):
        self.array_linspace = None
        self.array_random = None

    def crea_array_linspace(self):
        self.array_linspace = np.linspace(0, 1, 12)
        print("Array linspace:", self.array_linspace)

    def crea_array_casuale(self):
        self.array_random = np.random.rand(12)
        print("Array casuale:", self.array_random)

    def calcola_somme(self):
        somma_lin = np.sum(self.array_linspace)
        somma_rand = np.sum(self.array_random)
        print("Somma array linspace:", somma_lin)
        print("Somma array casuale:", somma_rand)

# Funzione principale
def main():
    esercizio = EsercizioArray()
    esercizio.crea_array_linspace()
    esercizio.crea_array_casuale()
    esercizio.calcola_somme()

# Esecuzione del programma
main()


#esercizio 2 "linspace, random, sum"

# Crea un array di 50 numeri equidistanti tra 0 e 10
arr1 = np.linspace(0, 10,)

# Crea un array di 50 numeri casuali tra 0 e 1
arr2 = np.random.rand(50)

# Somma i due array elemento per elemento
arr_sum = arr1 + arr2

# Calcola la somma totale degli elementi del nuovo array
sum_totale = np.sum(arr_sum)

# Calcola la somma degli elementi > 5
sum_maggiori_5 = np.sum(arr_sum[arr_sum > 5])

# Stampa tutto
print("Array linspace:", arr1)
print("Array casuale:", arr2)
print("Array somma:", arr_sum)
print("Somma totale:", sum_totale)
print("Somma dei valori > 5:", sum_maggiori_5)