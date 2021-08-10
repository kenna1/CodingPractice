#Given a string, return a new string where the first and last chars have been exchanged.

'''front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

#Define the string
str = "abracadabrw"
# if the string length is greater than 1
if len(str)>1:
    #concatenate the last + middle + first
    switchLetters = str[-1:] + str[1:-1] + str[:1]
else:
    #otherwise return the letter
    switchLetters = str
#print result
print (switchLetters)