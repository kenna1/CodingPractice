'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
'''

def diff21(n):
    differ = 0
    #difference betweeen n and 21
    differ = 21 - n
    if n > 21:
        # return absolute difference x -2 because differ will be a negative number as the result is negative
        differ = differ * (-2)

    return differ

print (diff21(23))