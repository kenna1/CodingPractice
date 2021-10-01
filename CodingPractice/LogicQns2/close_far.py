'''

Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
 Note: abs(num) computes the absolute value of a number.


close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''

def close_far(a, b, c):
    close = 0
    distant = False
# Find which is close (differing a by 1)
# Find which is far ( differing a and b by 2+)

    distanceAnB= a - b
    distanceAnC = a - c
    if abs(distanceAnB) <= 1:
        aToC = a - c
        bToC = b - c
        if abs(aToC) >= 2 and abs(bToC) >= 2:
            distant = True

    elif abs(distanceAnC) <= 1:
        aToB = a - b
        cToB = c - b
        if abs(aToB) >= 2 and abs(cToB) >= 2:
            distant = True


    return distant

print(close_far(1, 2, 3))

