#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DECORATORI E GENERATORI IN PYTHON

- Generatori base
- yield
- generator expression
- next()
- Decoratori base
- Decoratori con parametri
- Decoratori multipli
- Decoratori con *args e **kwargs
"""

import time
from functools import wraps


# ==============================================================
# 1. GENERATORE BASE
# ==============================================================

print("=== 1. Generatore Base ===")

def numeri():
    yield 1
    yield 2
    yield 3

for n in numeri():
    print(n)

print()


# ==============================================================
# 2. NEXT()
# ==============================================================

print("=== 2. next() ===")

gen = numeri()

print(next(gen))
print(next(gen))
print(next(gen))

print()


# ==============================================================
# 3. GENERATORE CON CICLO
# ==============================================================

print("=== 3. Generatore con ciclo ===")

def conta_fino_a(max_num):

    numero = 1

    while numero <= max_num:
        yield numero
        numero += 1

for n in conta_fino_a(5):
    print(n)

print()


# ==============================================================
# 4. GENERATORE DI NUMERI PARI
# ==============================================================

print("=== 4. Numeri pari ===")

def numeri_pari(max_num):

    for i in range(max_num + 1):

        if i % 2 == 0:
            yield i

for n in numeri_pari(10):
    print(n)

print()


# ==============================================================
# 5. GENERATOR EXPRESSION
# ==============================================================

print("=== 5. Generator Expression ===")

quadrati = (x ** 2 for x in range(5))

for q in quadrati:
    print(q)

print()


# ==============================================================
# 6. DECORATORE BASE
# ==============================================================

print("=== 6. Decoratore Base ===")

def decoratore(func):

    def wrapper():
        print("Prima")
        func()
        print("Dopo")

    return wrapper


@decoratore
def saluta():
    print("Ciao!")

saluta()

print()


# ==============================================================
# 7. DECORATORE CON PARAMETRI
# ==============================================================

print("=== 7. Decoratore con parametri ===")

def logger(func):

    def wrapper(*args, **kwargs):

        print("Funzione chiamata:", func.__name__)

        risultato = func(*args, **kwargs)

        print("Risultato:", risultato)

        return risultato

    return wrapper


@logger
def somma(a, b):
    return a + b

somma(5, 10)

print()


# ==============================================================
# 8. DECORATORE TIMER
# ==============================================================

print("=== 8. Timer ===")

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        risultato = func(*args, **kwargs)

        end = time.time()

        print("Tempo:", round(end - start, 6), "secondi")

        return risultato

    return wrapper


@timer
def operazione():

    totale = 0

    for i in range(1000000):
        totale += i

    return totale

operazione()

print()


# ==============================================================
# 9. DECORATORE CON PARAMETRO
# ==============================================================

print("=== 9. Decoratore parametrico ===")

def ripeti(volte):

    def decoratore(func):

        def wrapper(*args, **kwargs):

            for _ in range(volte):
                func(*args, **kwargs)

        return wrapper

    return decoratore


@ripeti(3)
def benvenuto():
    print("Benvenuto!")

benvenuto()

print()


# ==============================================================
# 10. DECORATORI MULTIPLI
# ==============================================================

print("=== 10. Decoratori Multipli ===")

def decoratore1(func):

    def wrapper(*args, **kwargs):

        print("Decoratore 1 INIZIO")

        risultato = func(*args, **kwargs)

        print("Decoratore 1 FINE")

        return risultato

    return wrapper


def decoratore2(func):

    def wrapper(*args, **kwargs):

        print("Decoratore 2 INIZIO")

        risultato = func(*args, **kwargs)

        print("Decoratore 2 FINE")

        return risultato

    return wrapper


@decoratore1
@decoratore2
def funzione_test():
    print("Funzione originale")


funzione_test()

print()


# ==============================================================
# 11. GENERATORE INFINITO
# ==============================================================

print("=== 11. Generatore infinito ===")

def contatore():

    numero = 1

    while True:
        yield numero
        numero += 1


gen = contatore()

for _ in range(5):
    print(next(gen))

print()


# ==============================================================
# 12. GENERATORE FIBONACCI
# ==============================================================

print("=== 12. Fibonacci ===")

def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):

        yield a

        a, b = b, a + b


for numero in fibonacci(10):
    print(numero)

print()


# ==============================================================
# 13. DECORATORE + GENERATORE
# ==============================================================

print("=== 13. Decoratore su Generatore ===")

def traccia_generatore(func):

    def wrapper(*args, **kwargs):

        print("Generatore avviato")

        yield from func(*args, **kwargs)

        print("Generatore terminato")

    return wrapper


@traccia_generatore
def genera_numeri():

    for i in range(1, 6):
        yield i


for numero in genera_numeri():
    print(numero)

print()


# ==============================================================
# 14. DECORATORE VALIDAZIONE
# ==============================================================

print("=== 14. Decoratore Validazione ===")

def controlla_positivo(func):

    def wrapper(numero):

        if numero < 0:
            print("Valore non valido")
            return None

        return func(numero)

    return wrapper


@controlla_positivo
def radice(numero):
    return numero ** 0.5

print(radice(25))
print(radice(-4))

print()


# ==============================================================
# 15. GENERATORE FILE SIMULATO
# ==============================================================

print("=== 15. Lettura simulata ===")

def leggi_righe():

    righe = [
        "Prima riga",
        "Seconda riga",
        "Terza riga"
    ]

    for riga in righe:
        yield riga


for riga in leggi_righe():
    print(riga)
