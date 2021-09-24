'''

Given 3 int values, a b c, return their sum.
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens.
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
'''

def fix_teen(n):
# check if n >=13 and n <15 or n > 16 and n <=19 ;  n = 0
    if n >= 13 and n < 15 or n > 16 and n <= 19:
        n = 0
# else; return n
    return n

def no_teen_sum(a, b, c):
# check if a is teen
    a = fix_teen(a)
# check if b is teen
    b = fix_teen(b)
# check if c is teen
    c = fix_teen(c)

# return the sum of a b c
    return a + b + c

print(no_teen_sum(2, 1, 15))
