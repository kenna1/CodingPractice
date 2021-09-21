'''

Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
return a string of the form "7:00" indicating when the alarm clock should ring.
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
'''


def alarm_clock(day, vacation):
#check if vacation is True
    time = ''
    seven = '7:00'
    ten = '10:00'
    off = 'off'
    if vacation == True:
    #if the day <= 7; return '10:00'
        if day > 0 and day < 6:
            time += ten
    #else; return 'off'
        else:
            time += off
#else if vacation is False
    else:
    #if the day <= 7 and vacation is false; return '7:00'
        if day > 0 and day < 6:
            time += seven
    #else; return '10:00'
        else:
            time += ten

    return time

print(alarm_clock(1, True))