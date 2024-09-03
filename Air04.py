import sys

def remove_adjacent_duplicates(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input should be a string")
    
    if not input_string:
        return input_string

    new_string = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i-1]:
            new_string += input_string[i]
    
    return new_string

def validate_and_process_input(input_string):
    if not isinstance(input_string, str):
        return False, "Input should be a string"

    if not input_string:
        return False, "Input string cannot be empty"

    return True, remove_adjacent_duplicates(input_string)


if len(sys.argv) != 2:
    print("Error: Exactly one argument required")
    print("Usage: python script.py '<input_string>'")
    sys.exit(1)

input_string = sys.argv[1]

is_valid, result = validate_and_process_input(input_string)

if is_valid:
    print("The string without adjacent duplicate characters is:", result)
else:
    print(f"Error: {result}")
    sys.exit(1)
