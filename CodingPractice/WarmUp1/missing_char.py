'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


'''

def missing_char(str, n):
# go through the string until you get to index n
# when you get to index n, remove the value in the index
# output the result

# --------------------------------------------------------------------------------------------------=======
# or using slicing
# get all letters until you reach the letter to be removed in index n
    str1 = str[:n]
# skip the index of the letter to be removed and print the remaineder of the string
    str2 = str[n+1:]
# join the strings together
    str1 += str2
    print(str1)

missing_char('kitten', 0)