import sys
import re

def is_valid_input(input_string):

    return len(input_string) > 0

def clean_input(input_string):
    return re.sub(r'[^A-Za-z0-9 ]+', '', input_string).split()

def ma_fonction(array_de_strings, separateur):
    return separateur.join(array_de_strings)

if len(sys.argv) != 2:
    print("Error: Exactly one argument required")
    print("Usage: python script.py '<phrase>'")
    sys.exit(1)
    
o = sys.argv[1]

if is_valid_input(o):
    words = clean_input(o)
    separateur = " "
    result = ma_fonction(words, separateur)
    print(result)
else:
    print("Error: Invalid input. Please provide a non-empty string.")
    sys.exit(1)
