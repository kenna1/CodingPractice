'''
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
'''

def non_start(a, b):
    newA = ""
    newB = ""
# Loop while less than a.len
    for l in range(1, len(a)):
    # add character to newA
        newA+= a[l]
# Loop while less than b.len
    for l in range(1, len(b)):
    # add character to newB
        newB += b[l]
# concatenate newA and new B
    return newA + newB

print(non_start('java', 'code'))