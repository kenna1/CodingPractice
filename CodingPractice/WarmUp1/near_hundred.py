'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''

def near_hundred(n):
    #if n is between 90-100 or 190-200
        # return True
    # How do we check if n is between 90-100
    # if n - 100 <= 10 or if n - 200 <= 10, then return true
    print(abs(n - 100))
    around100 = abs(n - 100)
    around200 = abs(n - 200)
    if around100 <= 10 or around200 <= 10:
        return True
    else:
        return False

print(near_hundred(190))