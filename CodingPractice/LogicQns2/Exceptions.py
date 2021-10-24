import math

def ex(n):
    try:
        print(math.sqrt(n))
    except:
        print("Bad Value for square root")
        print("Using absolute value instead")
        print(math.sqrt(abs(n)))

ex(-1)