#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ESEMPI BASE SULLE FUNZIONI IN PYTHON

- Definizione funzione
- Parametri
- Return
- Parametri di default
- *args
- **kwargs
- Lambda
- Ricorsione
- Funzioni come parametri
"""

# ==============================================================
# 1. FUNZIONE SEMPLICE
# ==============================================================

def saluta():
    print("Ciao a tutti!")

saluta()

print()


# ==============================================================
# 2. FUNZIONE CON PARAMETRI
# ==============================================================

def saluta_nome(nome):
    print("Ciao", nome)

saluta_nome("Mario")
saluta_nome("Anna")

print()


# ==============================================================
# 3. FUNZIONE CON RETURN
# ==============================================================

def somma(a, b):
    return a + b

risultato = somma(10, 20)

print("Somma:", risultato)

print()


# ==============================================================
# 4. PIÙ PARAMETRI
# ==============================================================

def area_rettangolo(base, altezza):
    return base * altezza

print("Area:", area_rettangolo(5, 4))

print()


# ==============================================================
# 5. PARAMETRI DI DEFAULT
# ==============================================================

def saluto(nome="Utente"):
    print("Benvenuto", nome)

saluto()
saluto("Luca")

print()


# ==============================================================
# 6. RETURN MULTIPLO
# ==============================================================

def operazioni(a, b):
    return a + b, a - b, a * b

somma, differenza, prodotto = operazioni(10, 5)

print("Somma:", somma)
print("Differenza:", differenza)
print("Prodotto:", prodotto)

print()


# ==============================================================
# 7. *ARGS
# ==============================================================

def somma_tutti(*numeri):

    totale = 0

    for numero in numeri:
        totale += numero

    return totale

print(somma_tutti(1, 2, 3))
print(somma_tutti(1, 2, 3, 4, 5))

print()


# ==============================================================
# 8. **KWARGS
# ==============================================================

def stampa_dati(**dati):

    for chiave, valore in dati.items():
        print(chiave, "=", valore)

stampa_dati(nome="Marco", eta=30, citta="Torino")

print()


# ==============================================================
# 9. FUNZIONE LAMBDA
# ==============================================================

quadrato = lambda x: x ** 2

print("Quadrato:", quadrato(5))

somma = lambda a, b: a + b

print("Somma:", somma(3, 4))

print()


# ==============================================================
# 10. FUNZIONE CHE CHIAMA ALTRA FUNZIONE
# ==============================================================

def quadrato(numero):
    return numero ** 2

def stampa_quadrato(numero):
    print(quadrato(numero))

stampa_quadrato(6)

print()


# ==============================================================
# 11. FUNZIONI COME PARAMETRI
# ==============================================================

def applica(funzione, valore):
    return funzione(valore)

def triplo(x):
    return x * 3

print(applica(triplo, 10))

print()


# ==============================================================
# 12. RICORSIONE
# ==============================================================

def fattoriale(n):

    if n == 0:
        return 1

    return n * fattoriale(n - 1)

print("Fattoriale:", fattoriale(5))

print()


# ==============================================================
# 13. FUNZIONE CON LISTA
# ==============================================================

def media(lista):

    return sum(lista) / len(lista)

numeri = [10, 20, 30, 40]

print("Media:", media(numeri))

print()


# ==============================================================
# 14. FUNZIONE CON CONDIZIONE
# ==============================================================

def pari_o_dispari(numero):

    if numero % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

print(pari_o_dispari(10))
print(pari_o_dispari(7))

print()


# ==============================================================
# 15. ESEMPIO PRATICO
# ==============================================================

def calcola_sconto(prezzo, percentuale):

    sconto = prezzo * percentuale / 100

    return prezzo - sconto

prezzo_finale = calcola_sconto(100, 20)

print("Prezzo finale:", prezzo_finale)
