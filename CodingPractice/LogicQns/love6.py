'''

The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6.
Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.


love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
'''

def love6(a, b):
    find6 = False
#check if 6 is a or b; return True
    if a == 6 or b == 6:
        find6 = True
#else; add the values a and b
    else:
        total = a - b
        diff = a + b

    # if total is = 6; return True
        if abs(total) == 6 or diff == 6:
            find6 = True
# return False
    return find6

print(love6(1,5))