'''

We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

'''

def make_bricks(small, big, goal):
    possible = False
# multiply small by 1
    small *= 1
# multiply big by 5
    big *= 5
# add new small and big and compare with goal
    total_bricks = small + big
    if total_bricks >= goal:
    # if equal, retun True
        possible = True
    #else; return false
    return possible

print(make_bricks(3, 2, 10))