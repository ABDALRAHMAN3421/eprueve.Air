import sys
import re

def trouver_valeur_impair(liste):
    for element in liste:
        if element % 2 != 0:
            return element
    return None

def is_valid_input_format(input_string):
    return re.fullmatch(r'[\d\s]+', input_string) is not None

def all_parts_are_digits(input_string):
    return all(part.isdigit() for part in input_string.split())

def process_input(input_string):
    if is_valid_input_format(input_string) and all_parts_are_digits(input_string):
        liste_test = list(map(int, input_string.split()))
        return trouver_valeur_impair(liste_test)
    else:
        return None


if len(sys.argv) != 2:
    print("Error: Exactly one argument required")
    print("Usage: python script.py '<numbers>'")
    sys.exit(1)

liste_test = sys.argv[1]
valeur_impair = process_input(liste_test)

if valeur_impair is not None:
    print("The first odd value in the list is:", valeur_impair)
else:
    print("Error: Invalid input or there are no odd values in the list.")
    sys.exit(1)
