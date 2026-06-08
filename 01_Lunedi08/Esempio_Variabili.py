#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ESEMPI BASE SULLE VARIABILI IN PYTHON

- Variabili numeriche
- Stringhe
- Booleani
- Conversioni
- Operazioni
- Assegnazioni multiple
"""

# ==============================================================
# 1. VARIABILI INTERE
# ==============================================================

eta = 25
anno = 2025

print("Età:", eta)
print("Anno:", anno)
print()


# ==============================================================
# 2. VARIABILI DECIMALI
# ==============================================================

prezzo = 19.99
temperatura = 24.5

print("Prezzo:", prezzo)
print("Temperatura:", temperatura)
print()


# ==============================================================
# 3. STRINGHE
# ==============================================================

nome = "Mario"
cognome = "Rossi"

print("Nome:", nome)
print("Cognome:", cognome)
print()


# ==============================================================
# 4. BOOLEANI
# ==============================================================

attivo = True
maggiorenne = False

print("Attivo:", attivo)
print("Maggiorenne:", maggiorenne)
print()


# ==============================================================
# 5. CONTROLLO DEL TIPO
# ==============================================================

numero = 10
testo = "Python"

print(type(numero))
print(type(testo))
print()


# ==============================================================
# 6. ASSEGNAZIONE MULTIPLA
# ==============================================================

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)
print()


# ==============================================================
# 7. STESSO VALORE A PIÙ VARIABILI
# ==============================================================

x = y = z = 100

print(x)
print(y)
print(z)
print()


# ==============================================================
# 8. OPERAZIONI NUMERICHE
# ==============================================================

n1 = 10
n2 = 5

print("Somma:", n1 + n2)
print("Differenza:", n1 - n2)
print("Prodotto:", n1 * n2)
print("Divisione:", n1 / n2)
print()


# ==============================================================
# 9. CONCATENAZIONE STRINGHE
# ==============================================================

nome = "Anna"
cognome = "Verdi"

completo = nome + " " + cognome

print(completo)
print()


# ==============================================================
# 10. CASTING
# ==============================================================

numero_testo = "123"

numero_intero = int(numero_testo)
numero_decimale = float(numero_testo)

print(numero_intero)
print(numero_decimale)
print()


# ==============================================================
# 11. F-STRING
# ==============================================================

nome = "Luca"
eta = 30

print(f"{nome} ha {eta} anni")
print()


# ==============================================================
# 12. SCAMBIO DI VARIABILI
# ==============================================================

a = 10
b = 20

print("Prima:", a, b)

a, b = b, a

print("Dopo:", a, b)
print()


# ==============================================================
# 13. VARIABILI DINAMICHE
# ==============================================================

dato = 10
print(dato, type(dato))

dato = "Ciao"
print(dato, type(dato))

dato = True
print(dato, type(dato))
print()


# ==============================================================
# 14. COSTANTI (CONVENZIONE)
# ==============================================================

PI_GRECO = 3.14159
MAX_UTENTI = 100

print(PI_GRECO)
print(MAX_UTENTI)
