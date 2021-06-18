import sys

def add_plus_ten(x, y):
    return x + y + 10

def custom_print():
    version_number = sys.version_info
    word =''
    if version_number.major == 2:
        word = input("Please enter your word: ")
    elif version_number.major == 3:
        word = input("Please enter your word: ")
    else:
        pass
    print(word)

custom_print()

#result = add_plus_ten(10, 67)
#print(result)