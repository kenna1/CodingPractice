'''
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def last2(str):
# Get the last two characters of the string and store in variable
    last2Char = str[-2:]
    counter = 0
    i = 0
    j = 2
# Loop while less than the length - 2
    while i < len(str)-2:
        # if substring(i,j) == variable
        if str[i:j] == last2Char:
        #increment counter
            counter+=1
        #increment substring indices
        j+=1
        i+=1

# return counter
    return counter

print(last2('axxxaaxx'))