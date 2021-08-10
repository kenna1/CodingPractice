'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

'''

def not_string(str):
#check if the string begins with not
    if str[0:3] == "not":
#if yes,
    #return string
        return str
#if no,
    else:
    # concatenate not and new word
        return "not" + " " + str
    # return new word

print (not_string("not me"))