'''

Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
'''

def has23(nums):
#check if element 1 is 2 or 3
#check if element 2 is 2 or 3
#return True
    return (nums[0] == 2 or nums[0]==3 or nums[1] == 2 or nums[1]==3 )

print(has23([4, 5]))