import random

# ----------------------------------------
# FUNZIONE 1
# Chiede un numero intero positivo
# Se il numero è <= 0, continua a richiederlo
# ----------------------------------------
def chiedi_numero_positivo():
    numero = int(input("Inserisci un numero intero positivo: "))

    while numero <= 0:
        print("Errore: il numero deve essere maggiore di 0.")
        numero = int(input("Inserisci un numero intero positivo: "))

    return numero


# ----------------------------------------
# FUNZIONE 2
# Genera una lista lunga n
# con numeri casuali tra 1 e n
# ----------------------------------------
def genera_lista(n):
    lista = []

    for i in range(n):
        numero_casuale = random.randint(1, n)
        lista.append(numero_casuale)

    return lista


# ----------------------------------------
# FUNZIONE 3
# Calcola la somma dei numeri pari nella lista
# ----------------------------------------
def somma_pari(lista):
    somma = 0

    for numero in lista:
        if numero % 2 == 0:
            somma = somma + numero

    return somma


# ----------------------------------------
# FUNZIONE 4
# Stampa tutti i numeri dispari nella lista
# ----------------------------------------
def stampa_dispari(lista):
    print("Numeri dispari nella lista:")

    for numero in lista:
        if numero % 2 != 0:
            print(numero)


# ----------------------------------------
# FUNZIONE 5
# Controlla se un numero è primo
# Restituisce True se è primo, False altrimenti
# ----------------------------------------
def numero_primo(numero):
    if numero <= 1:
        return False

    for divisore in range(2, numero):
        if numero % divisore == 0:
            return False

    return True


# ----------------------------------------
# FUNZIONE 6
# Stampa tutti i numeri primi presenti nella lista
# ----------------------------------------
def stampa_primi(lista):
    print("Numeri primi nella lista:")

    for numero in lista:
        if numero_primo(numero) == True:
            print(numero)


# ----------------------------------------
# FUNZIONE 7
# Calcola la somma di tutti i numeri primi nella lista
# ----------------------------------------
def somma_primi(lista):
    somma = 0

    for numero in lista:
        if numero_primo(numero) == True:
            somma = somma + numero

    return somma


# ----------------------------------------
# FUNZIONE MENU
# Mostra le opzioni disponibili
# ----------------------------------------
def mostra_menu():
    print("\n--- MENU ---")
    print("1 - Mostra lista")
    print("2 - Somma dei numeri pari")
    print("3 - Stampa numeri dispari")
    print("4 - Verifica se un numero è primo")
    print("5 - Stampa numeri primi nella lista")
    print("6 - Somma dei numeri primi nella lista")
    print("esci - Termina il programma")


# ----------------------------------------
# PROGRAMMA PRINCIPALE
# ----------------------------------------

# Punto 1 obbligatorio: input iniziale
n = chiedi_numero_positivo()

# Punto 2: generazione lista
lista_numeri = genera_lista(n)

print("\nLista generata:", lista_numeri)

# Il programma continua finché l'utente non scrive esci
scelta = ""

while scelta != "esci":

    mostra_menu()

    scelta = input("Scegli un'opzione: ")

    match scelta:

        case "1":
            print("Lista:", lista_numeri)

        case "2":
            risultato = somma_pari(lista_numeri)
            print("Somma dei numeri pari:", risultato)

        case "3":
            stampa_dispari(lista_numeri)

        case "4":
            numero = int(input("Inserisci un numero da controllare: "))

            if numero_primo(numero) == True:
                print(numero, "è un numero primo")
            else:
                print(numero, "non è un numero primo")

        case "5":
            stampa_primi(lista_numeri)

        case "6":
            risultato = somma_primi(lista_numeri)
            print("Somma dei numeri primi:", risultato)

        case "esci":
            print("Programma terminato.")

        case _:
            print("Scelta non valida.")
