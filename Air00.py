import sys

def my_function(string_to_cut, string_separator):
    if string_separator in string_to_cut:
        new_list = string_to_cut.split(string_separator)
        return new_list, True
    else:
        return "Error", False

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <string_to_cut> <string_separator>")
        return
    
    string_to_cut = sys.argv[1]
    string_separator = sys.argv[2]
    
    result, success = my_function(string_to_cut, string_separator)
    if success:
        print(result)
    else:
        print(result)

main()
