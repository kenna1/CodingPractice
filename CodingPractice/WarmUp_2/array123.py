'''

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

'''

def array123(nums):
    one, two, three = 0, 0, 0
# Go through the array
    #Loop through array while less than array length
    for i  in range(0, len(nums)):
        #check if 1, 2, 3 exist
        # if array[n] == 1, record the index "one"
        if nums[i] == 1:
            one = i

        # if array[n] == 2, record the index "two"
        if nums[i] == 2:
            two = i

        # if array[n] == 3, record the index "three"
        if nums[i] == 3:
            three = i

    print(one)
    print(two)
    print(three)


    # if yes, return true, else false
        #if three - two == 1 and two - one == 1
    if three - two == 1 and two - one == 1:
            #return true
        return True
        #else return false
    else:
        return False

print(array123([1, 1, 2, 3, 1]))