'''
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

'''

def common_end(a, b):
# if a[1] or b[1] are equal and if b[-1] or a[-1] are equal
    if a[0] == b[0] or b[-1] == a[-1]:
    #return True
        return True
# else
    else:
    #return False
        return False


print(common_end([1, 2, 3], [7, 3, 1]))