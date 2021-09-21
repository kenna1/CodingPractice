'''

You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.


caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
'''

def caught_speeding(speed, is_birthday):
    ticket = 0
    limit60 = 60
    limit80minus = 80
    limit80plus = 81

#check if it's birthday; if so, add 5
    if is_birthday == True:
        limit60+=5
        limit80minus+=5
        limit80plus+=5

#if speed is > 61 and less than 80 inclusive; result is 1
    if speed > limit60 and speed <=limit80minus:
        ticket = 1
#if speed is 81 or more, the result is 2
    elif speed >= limit80plus:
        ticket = 2
# if anything less than 60, return ticket 0
    return ticket

print(caught_speeding(65, True))