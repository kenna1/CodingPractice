'''

Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]

'''

def rotate_left3(nums):
    store = nums[0]
# put the second element in the first position
    nums[0] = nums[1]
# and the third element in the second position
    nums[1] = nums[2]
# first in the third
    nums[2] = store
# return new array
    return nums

print(rotate_left3([5, 11, 9]))