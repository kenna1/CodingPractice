'''

Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
'''

def sorta_sum(a,b):
# caluclate sum a and b
    sum = a + b
# if sum is >= 10 and <= 19;  return 20
    if sum >=10 and sum<=19:
        sum = 20
# else
    # return sum
    return sum


print(sorta_sum(10, 11))