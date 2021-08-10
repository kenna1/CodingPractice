'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''

def makes10(a, b):
    tenner = False
    sum = a + b
#check if a is 10 or if b is 10
    if a == 10 or b == 10:
        # return true
        tenner = True
# add the two
# if sum is 10 return true
    elif sum == 10:
        tenner = True
    return tenner

print("{}, {}, {}".format(makes10(9, 10),
makes10(9, 9),
makes10(1, 9)))