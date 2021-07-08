'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double(a, b):
    # get the sum
    sum = a + b
    # if a is equal to b
    if a == b:
        # return sum * 2
        sum *= 2
    # otherwise
    return sum
    # return sum

print(sum_double(2, 2))