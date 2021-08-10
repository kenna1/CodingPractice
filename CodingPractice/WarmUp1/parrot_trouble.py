'''

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''

def parrot_trouble(talking, hour):
# if talking is true and hour is before 7
    if talking and hour < 7:
        print (talking)
    # then true because we are in trouble
        return True
# if talking is true and hour is after 20
    if talking and hour > 20:
    # then true; we are in trouble
        return True
    else:
        return False


print("{}, {}, {}".format(parrot_trouble(True, 6),
parrot_trouble(True, 7),
parrot_trouble(False, 6)
))