'''


Given an array of ints, return the sum of the first 2 elements in the array.
 If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2

'''


def sum2(nums):
    sum = 0
# if length of the array > 1
    if len(nums) > 1:
    # add first two element
        sum = nums[0] + nums[1]
# else if == 1
    elif len(nums) == 1:
    # add first element
        sum += nums[0]

    return sum

print(sum2([1,1,1,1]))