'''

Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''

def lone_sum(a, b, c):
    sum = a + b + c
# check if the values are equal; if so, remove them from the sum
    # check if a == b and a == c ; remove a b and from sum
    if a == b and a == c:
        sum = sum - a - b - c
    #else
    else:
        # check if a == b ; remove a and b from sum
        if a == b:
            sum = sum - a - b
        # else check if a = c ; remove a and c from the sum
        if a == c:
            sum = sum - a - c
        # check if b == c; remove b and c from sum
        if b == c:
            sum = sum - b - c

# return total sum
    return sum

print(lone_sum(3, 3, 3))