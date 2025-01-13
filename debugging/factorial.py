#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémente n pour éviter une boucle infinie
    return result

if len(sys.argv) > 1:
    try:
        input_value = int(sys.argv[1])
        if input_value < 0:
            print("Erreur : la factorielle n'est pas définie pour les nombres négatifs.")
        else:
            f = factorial(input_value)
            print(f)
    except ValueError:
        print("Erreur : veuillez entrer un entier valide.")
else:
    print("Utilisation : ./factorial.py <nombre>")
