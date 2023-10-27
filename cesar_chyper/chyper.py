import string


def get_symbol_table_list ():
    return list(string.printable)


def encode_to_cesar (password, key):
    for char in password:
        print(char)


print("encoded password", encode_to_cesar(input("enter the password:\n"), 3))
