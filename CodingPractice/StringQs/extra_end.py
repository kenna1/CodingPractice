'''

Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
'''

def extra_end(str):
#get the substring of the last two characters
    last2 = str[-2:]
#return las2 characters 3 times
    return last2 * 3

print(extra_end("ab"))