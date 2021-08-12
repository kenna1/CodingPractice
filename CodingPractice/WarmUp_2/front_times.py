'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(str, n):
    # find the first 3 characters and store in variable c
        str3 = str[0:3]
    #initialising newStr for new String
        newStr = ""
    # loop through array: while iterator is less than n
        i = 0
        while(i < n):
            # Add 3 characters to new variable
            newStr += str3
            # increment iterator
            i+=1
# return new variable
        return newStr


print(front_times("C", 3))