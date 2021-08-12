'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
#while counter is not equal to n
    i = 0
    newStr = ""
    while i < n:
    #print str
        #Add string to newString
        newStr+=str
        i+=1
    return newStr

print (string_times("Hi", 0))