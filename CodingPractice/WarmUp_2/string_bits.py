'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''
def string_bits(str):
    #declare a string A
    strA = ""
    i = 0
    #Loop through string
    while i < len(str):
    #if second letter, skip
    #if i % 2 == 0
        if i % 2 == 0:
            #A = A + character
            strA += str[i]
            #increment
        i+=1
    #return A
    return strA

print(string_bits("Heeololeo"))
