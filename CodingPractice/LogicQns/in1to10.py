'''

Given a number n, return True if n is in the range 1..10, inclusive.
Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True

'''

def in1to10(n, outside_mode):
    inclusive = False
# Check if ouside range is on.
    if outside_mode == True:
    # if so, check if n is <= 1 or n >= 10; return True
        if n <= 1 or n >=10:
            inclusive = True
# else; check if n is between 1 to 10; return True
    elif n >= 1 and n <= 10:
        inclusive = True
    return inclusive

print(in1to10(-2, False))