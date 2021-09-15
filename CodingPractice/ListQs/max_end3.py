'''

Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]

'''

def max_end3(nums):
    newArray = []
# check if element[0] is greater than [3]
    if nums[0] > nums[2]:
    #then
        #new array = element [0] three times
        newNums = [nums[0], nums[0], nums[0]]
    #else
    else:
        #new array = element [2] three times
        newNums = [nums[2], nums[2], nums[2]]
    return newNums

print(max_end3([11, 5, 9]))