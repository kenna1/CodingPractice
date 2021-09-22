'''

Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
'''

def near_ten(num):
    rem2 = False
# divide ten and n, then get the remainder
    remainder = num % 10
# if the remainder is less than 2 ; return True (above the divisor)
    if remainder <= 2:
        rem2 = True
    # else ; minus 10 from remainder and check if its == 2
    else:
        within = 10 - remainder
        if within <= 2:
            rem2 = True
    return rem2

print(near_ten(31))