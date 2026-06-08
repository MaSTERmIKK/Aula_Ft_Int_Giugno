#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ESEMPI BASE SUI CICLI IN PYTHON

- for
- while
- range
- break
- continue
- pass
- enumerate
- zip
- cicli annidati
"""

# ==============================================================
# 1. FOR BASE
# ==============================================================

print("=== FOR BASE ===")

for i in range(5):
    print(i)

print()


# ==============================================================
# 2. RANGE
# ==============================================================

print("=== RANGE ===")

for i in range(1, 6):
    print(i)

print()

for i in range(0, 11, 2):
    print(i)

print()


# ==============================================================
# 3. WHILE
# ==============================================================

print("=== WHILE ===")

contatore = 1

while contatore <= 5:
    print(contatore)
    contatore += 1

print()


# ==============================================================
# 4. BREAK
# ==============================================================

print("=== BREAK ===")

for i in range(10):

    if i == 5:
        break

    print(i)

print()


# ==============================================================
# 5. CONTINUE
# ==============================================================

print("=== CONTINUE ===")

for i in range(6):

    if i == 3:
        continue

    print(i)

print()


# ==============================================================
# 6. PASS
# ==============================================================

print("=== PASS ===")

for i in range(3):

    if i == 1:
        pass

    print(i)

print()


# ==============================================================
# 7. CICLO SU STRINGA
# ==============================================================

print("=== STRINGA ===")

testo = "Python"

for lettera in testo:
    print(lettera)

print()


# ==============================================================
# 8. CICLO SU LISTA
# ==============================================================

print("=== LISTA ===")

numeri = [10, 20, 30, 40]

for numero in numeri:
    print(numero)

print()


# ==============================================================
# 9. ENUMERATE
# ==============================================================

print("=== ENUMERATE ===")

nomi = ["Anna", "Luca", "Marco"]

for indice, nome in enumerate(nomi):
    print(indice, nome)

print()


# ==============================================================
# 10. ZIP
# ==============================================================

print("=== ZIP ===")

nomi = ["Anna", "Luca", "Marco"]
eta = [20, 25, 30]

for nome, anni in zip(nomi, eta):
    print(nome, anni)

print()


# ==============================================================
# 11. CICLI ANNIDATI
# ==============================================================

print("=== CICLI ANNIDATI ===")

for i in range(3):

    for j in range(2):

        print("i =", i, "j =", j)

print()


# ==============================================================
# 12. FOR SU DIZIONARIO
# ==============================================================

print("=== DIZIONARIO ===")

persona = {
    "nome": "Anna",
    "eta": 25,
    "citta": "Roma"
}

for chiave, valore in persona.items():
    print(chiave, ":", valore)

print()


# ==============================================================
# 13. FOR ELSE
# ==============================================================

print("=== FOR ELSE ===")

for i in range(3):
    print(i)
else:
    print("Ciclo terminato")

print()


# ==============================================================
# 14. WHILE ELSE
# ==============================================================

print("=== WHILE ELSE ===")

x = 1

while x <= 3:
    print(x)
    x += 1
else:
    print("While terminato")

print()


# ==============================================================
# 15. ESEMPIO PRATICO
# ==============================================================

print("=== SOMMA NUMERI ===")

numeri = [5, 10, 15, 20]

somma = 0

for numero in numeri:
    somma += numero

print("Somma totale:", somma)
