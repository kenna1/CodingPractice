'''

Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''
def pos_neg(a, b, negative):

    condition = False

    #check if a is less than 0 and b is greater than 0; then return True
    if a < 0 and b >= 0:
        condition = True
    #check if a is greater than or equal to 0 and if b is less than 0; then condition is True
    elif a >= 0 and b < 0 :
        condition = True
    #or else check if the param negative is True. If so, then check if a and b are negative. if so, then condition is True
    elif negative == True:
        if a < 0 and b < 0:
            condition = True
    # return the value of condition at the end of all.
    return condition


print(pos_neg(1, --1, True))


'''elif a < 0
    if a and b < 0:
        notOpposite = True
        if negative == True:
            #return True
            condition = True
    #else 
        #return True
   aLessThan = False
    aGreaterThan = False
    bLessThan = False
    bGreaterThan = False
    opposite = False
#check if a is negative or positive       
    #check if a is less than 0
    if a < 0: 
        # negative is True
        aLessThan = True
    # or else
    else:
        # positive is True
        aGreaterThan = True
#check if b is positive or negative
    # check if b is less than 0
    if b < 0:
        # negative is True
        bLessThan = True
    # else
    else:
        # positive is True
        bGreaterThan = True
        
#check if a and b are not negative. If so, return true
#check if a and b are negative, then is negative is 'True'
    if lessThan == greaterThan:
    # check if a and b are less than 0
        # if True, then check if negative is True
        if negative == True:
             # then return true
   '''

