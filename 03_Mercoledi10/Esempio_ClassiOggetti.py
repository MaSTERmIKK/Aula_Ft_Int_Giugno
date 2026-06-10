#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLASSI, OGGETTI E METODI SPECIALI (__xxx__)

- Classi e oggetti
- Costruttore (__init__)
- Metodo di istanza
- Variabili di istanza
- Variabili di classe
- __str__
- __repr__
- __len__
- __eq__
- __lt__
- __add__
- __contains__
- __call__
- __del__
"""


# ==============================================================
# 1. CLASSE E OGGETTO
# ==============================================================

print("=== 1. Classe e Oggetto ===")

class Persona:

    def saluta(self):
        print("Ciao!")

p = Persona()
p.saluta()

print()


# ==============================================================
# 2. COSTRUTTORE (__init__)
# ==============================================================

print("=== 2. __init__ ===")

class Studente:

    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

s = Studente("Mario", 28)

print(s.nome)
print(s.voto)

print()


# ==============================================================
# 3. METODI DI ISTANZA
# ==============================================================

print("=== 3. Metodi ===")

class Rettangolo:

    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

r = Rettangolo(5, 4)

print("Area:", r.area())

print()


# ==============================================================
# 4. VARIABILE DI CLASSE
# ==============================================================

print("=== 4. Variabile di classe ===")

class Auto:

    ruote = 4

    def __init__(self, modello):
        self.modello = modello

a1 = Auto("Fiat")
a2 = Auto("BMW")

print(a1.ruote)
print(a2.ruote)

print()


# ==============================================================
# 5. __str__
# ==============================================================

print("=== 5. __str__ ===")

class Libro:

    def __init__(self, titolo):
        self.titolo = titolo

    def __str__(self):
        return f"Libro: {self.titolo}"

libro = Libro("Python Base")

print(libro)

print()


# ==============================================================
# 6. __repr__
# ==============================================================

print("=== 6. __repr__ ===")

class Prodotto:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Prodotto('{self.nome}')"

p = Prodotto("Mouse")

print(repr(p))

print()


# ==============================================================
# 7. __len__
# ==============================================================

print("=== 7. __len__ ===")

class Squadra:

    def __init__(self, giocatori):
        self.giocatori = giocatori

    def __len__(self):
        return len(self.giocatori)

s = Squadra(["Anna", "Luca", "Marco"])

print(len(s))

print()


# ==============================================================
# 8. __eq__
# ==============================================================

print("=== 8. __eq__ ===")

class Punto:

    def __init__(self, x):
        self.x = x

    def __eq__(self, altro):
        return self.x == altro.x

p1 = Punto(10)
p2 = Punto(10)

print(p1 == p2)

print()


# ==============================================================
# 9. __lt__
# ==============================================================

print("=== 9. __lt__ ===")

class Numero:

    def __init__(self, valore):
        self.valore = valore

    def __lt__(self, altro):
        return self.valore < altro.valore

n1 = Numero(5)
n2 = Numero(10)

print(n1 < n2)

print()


# ==============================================================
# 10. __add__
# ==============================================================

print("=== 10. __add__ ===")

class Vettore:

    def __init__(self, x):
        self.x = x

    def __add__(self, altro):
        return Vettore(self.x + altro.x)

    def __str__(self):
        return str(self.x)

v1 = Vettore(5)
v2 = Vettore(7)

print(v1 + v2)

print()


# ==============================================================
# 11. __contains__
# ==============================================================

print("=== 11. __contains__ ===")

class Archivio:

    def __init__(self):
        self.dati = ["Anna", "Luca", "Marco"]

    def __contains__(self, elemento):
        return elemento in self.dati

a = Archivio()

print("Anna" in a)
print("Paolo" in a)

print()


# ==============================================================
# 12. __call__
# ==============================================================

print("=== 12. __call__ ===")

class Moltiplicatore:

    def __call__(self, a, b):
        return a * b

m = Moltiplicatore()

print(m(3, 4))

print()


# ==============================================================
# 13. __del__
# ==============================================================

print("=== 13. __del__ ===")

class Test:

    def __del__(self):
        print("Oggetto eliminato")

t = Test()

del t

print()


# ==============================================================
# 14. PIÙ METODI SPECIALI INSIEME
# ==============================================================

print("=== 14. Classe Completa ===")

class StudenteCompleto:

    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def __str__(self):
        return f"{self.nome} ({self.voto})"

    def __repr__(self):
        return f"StudenteCompleto('{self.nome}', {self.voto})"

    def __eq__(self, altro):
        return self.voto == altro.voto

    def __lt__(self, altro):
        return self.voto < altro.voto

s1 = StudenteCompleto("Anna", 28)
s2 = StudenteCompleto("Luca", 30)

print(s1)
print(repr(s1))
print(s1 == s2)
print(s1 < s2)

print()


# ==============================================================
# 15. SORT CON __lt__
# ==============================================================

print("=== 15. Ordinamento Oggetti ===")

studenti = [
    StudenteCompleto("Marco", 22),
    StudenteCompleto("Anna", 30),
    StudenteCompleto("Luca", 25)
]

studenti.sort()

for studente in studenti:
    print(studente)
