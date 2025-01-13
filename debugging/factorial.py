#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Erreur : la factorielle n'est pas définie pour les nombres négatifs.")
    else:
        f = factorial(n)
        print(f)
except ValueError:
    print("Erreur : veuillez entrer un nombre entier.")
except IndexError:
    print("Erreur : veuillez fournir un argument pour calculer la factorielle.")
