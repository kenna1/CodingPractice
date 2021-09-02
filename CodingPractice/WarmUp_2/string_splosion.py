"""

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

"""
def string_splosion(str):

# Declare a new String
    str1 = ""
# Declare iterator
    i = 1
# Loop while less than or equal to length of string
    while i <= len(str):
        # concatenate the first letter, then first two letters, then first 3 letters, until it has reached the end to new string
        str1+=str[:i]
        # increment iterator
        i+=1
    #return new string
    return str1


print(string_splosion("code"))