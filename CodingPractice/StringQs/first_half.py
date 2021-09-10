'''

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

'''

def first_half(str):
# Divide the string into two and store it in a variable
    half = len(str)//2
# get the first half
    firstH = str[:half]
# return variable
    return firstH

print(first_half("HelloThere"))