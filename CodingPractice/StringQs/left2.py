'''

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
'''

def left2(str):
# concatenate last two letters and first few letters before the last two
    firstH = str[:2]
    secondH = str[2:]
# return concatenation
    return  secondH + firstH

print(left2('Hi'))