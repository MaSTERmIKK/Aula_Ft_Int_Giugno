#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CONDIZIONI E MATCH IN PYTHON

- if
- if else
- if elif else
- operatori di confronto
- operatori logici
- condizioni annidate
- operatore ternario
- match case
"""

# ==============================================================
# 1. IF SEMPLICE
# ==============================================================

eta = 20

if eta >= 18:
    print("Maggiorenne")

print()


# ==============================================================
# 2. IF ELSE
# ==============================================================

numero = 7

if numero % 2 == 0:
    print("Numero pari")
else:
    print("Numero dispari")

print()


# ==============================================================
# 3. IF ELIF ELSE
# ==============================================================

voto = 27

if voto >= 28:
    print("Ottimo")
elif voto >= 24:
    print("Buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")

print()


# ==============================================================
# 4. OPERATORI DI CONFRONTO
# ==============================================================

a = 10
b = 20

print(a == b)   # uguale
print(a != b)   # diverso
print(a > b)    # maggiore
print(a < b)    # minore
print(a >= b)   # maggiore uguale
print(a <= b)   # minore uguale

print()


# ==============================================================
# 5. OPERATORI LOGICI
# ==============================================================

eta = 25
studente = True

if eta >= 18 and studente:
    print("Maggiorenne e studente")

if eta >= 18 or studente:
    print("Almeno una condizione vera")

if not studente:
    print("Non è studente")

print()


# ==============================================================
# 6. CONDIZIONI ANNIDATE
# ==============================================================

numero = 12

if numero > 0:
    if numero % 2 == 0:
        print("Positivo e pari")

print()


# ==============================================================
# 7. OPERATORE TERNARIO
# ==============================================================

numero = 15

risultato = "Pari" if numero % 2 == 0 else "Dispari"

print(risultato)

print()


# ==============================================================
# 8. MATCH BASE
# ==============================================================

giorno = 3

match giorno:
    case 1:
        print("Lunedì")
    case 2:
        print("Martedì")
    case 3:
        print("Mercoledì")
    case _:
        print("Altro giorno")

print()


# ==============================================================
# 9. MATCH CON STRINGHE
# ==============================================================

comando = "start"

match comando:
    case "start":
        print("Avvio programma")
    case "stop":
        print("Arresto programma")
    case _:
        print("Comando sconosciuto")

print()


# ==============================================================
# 10. MATCH CON PIÙ VALORI
# ==============================================================

voto = 30

match voto:
    case 30 | 31:
        print("Eccellente")
    case 28 | 29:
        print("Ottimo")
    case _:
        print("Altro voto")

print()


# ==============================================================
# 11. MATCH CON GUARD (CONDIZIONE)
# ==============================================================

numero = 11

match numero:
    case n if n % 2 == 0:
        print("Pari")
    case n if n % 2 != 0:
        print("Dispari")

print()


# ==============================================================
# 12. MATCH CON TUPLE
# ==============================================================

punto = (0, 5)

match punto:
    case (0, 0):
        print("Origine")
    case (0, y):
        print("Asse Y:", y)
    case (x, 0):
        print("Asse X:", x)
    case _:
        print("Punto generico")

print()


# ==============================================================
# 13. MATCH CON LISTE
# ==============================================================

lista = [1, 2]

match lista:
    case [1, 2]:
        print("Lista [1,2]")
    case [1, x]:
        print("Lista che inizia per 1 e termina con", x)
    case _:
        print("Altra lista")

print()


# ==============================================================
# 14. MATCH CON DIZIONARI
# ==============================================================

utente = {
    "nome": "Anna",
    "eta": 25
}

match utente:
    case {"nome": nome, "eta": eta}:
        print(f"{nome} ha {eta} anni")
    case _:
        print("Formato sconosciuto")

print()


# ==============================================================
# 15. ESEMPIO PRATICO MENU
# ==============================================================

scelta = 2

match scelta:
    case 1:
        print("Visualizza utenti")
    case 2:
        print("Aggiungi utente")
    case 3:
        print("Elimina utente")
    case _:
        print("Scelta non valida")
