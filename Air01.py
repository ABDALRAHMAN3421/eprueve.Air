import sys

def my_function(string_to_cut, string_separator):
    if string_separator.isdigit():
        return ["Error"]
    array = string_to_cut.split(string_separator)
    return array


if len(sys.argv) != 3:
    print("Usage: python script.py <string_to_cut> <string_separator>")
    sys.exit(1)

string_to_cut = sys.argv[1]
string_separator = sys.argv[2]

result = my_function(string_to_cut, string_separator)

for part in result:
    print(part)

