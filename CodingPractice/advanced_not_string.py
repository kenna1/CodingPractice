'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
Exceptions are words like "nottingham", "nothing"

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
not_string('nottingham') → 'not nottingham'


'''

def not_string(str):
#check if the string begins with not
    if str[0:4] == "not ":
#if yes,
    #return string
        return str
#check if the word has not at the start without a space
    elif str[0:3] == "not":
        #if yes, return not + word
        return "not" + " " + str
#if no,
    else:
    # otherwise concatenate not and new word
        return "not" + " " + str
    # return new word

print (not_string("nothing"))