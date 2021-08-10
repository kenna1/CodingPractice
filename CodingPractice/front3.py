'''
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
'''

def front3(str):

#Find the first 3 characters
    newStr = str[0:3]
#Print it 3 times using concatenation
    concatStr = newStr+newStr+newStr
    print(concatStr)

front3("abc")
