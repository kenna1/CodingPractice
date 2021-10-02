'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''

def make_chocolate(small, big, goal):
# multiply the big bar by 5
    big *= 5
# Multiply the small bars by 1
    small *= 1
# Minus the big bar from the goal, store in result
    result = big - goal
# if number of small bar is less than result; return -1
    if small < abs(result):
        result = -1
# else return result
    else:
        result = abs(result)

    return result


print(make_chocolate(6, 2, 7))