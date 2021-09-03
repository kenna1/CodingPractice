'''
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

'''

def array_count9(nums):
# Go through an array
    count = 0
    # Loop while less than the array length
    for n in nums:
        #if array[i] == 9
        if n == 9:
            #increment count
            count+=1
# Count the number of 9's
    # return count
    return count

print(array_count9([1, 9, 9, 3, 9]))