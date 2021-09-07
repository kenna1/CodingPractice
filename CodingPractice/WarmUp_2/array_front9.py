"""

Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

"""

def array_front9(nums):
    i = 0
    num9 = False
# Loop through the array by slicing the first 4
    print(nums[:4])
    for n in nums[:4]:
        # if we find 9, return true, else return false
        if n == 9:
            num9 = True

    return num9




print(array_front9([1, 2, 2, 3, 9]))
