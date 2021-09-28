'''

For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
Given 3 ints, a b c, return the sum of their rounded values.
To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
Write the helper entirely below and at the same indent level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
'''

def round_sum(a, b, c):
    #add a b c rounded
    x = round10(a)
    y = round10(b)
    z = round10(c)

    return x + y + z

def round10(num):
# Divide the number by 10 and keep the remainder
    rem = num%10
    newNum = 0
    if rem >= 5:
        # minus the remainder by 10
        x = 10 - rem
        # add that number to original number if greater than 5
        newNum = num + x
    else:
        newNum = num - rem

    return newNum

print(round_sum(45, 21, 30))