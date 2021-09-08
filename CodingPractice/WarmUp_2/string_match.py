'''

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

'''

def string_match(a, b):
    #Declare variables for the starting index i
    i = 0
    # j will observe the next character
    j = 1
    # Declare counter to count the number of similar substrings of 2
    count = 0
    # while i is less than the length of the first string a
    while i < len(a)-1:
        #increment j to find substring of length 2
        j += 1
        # compare the substring of length 2 in both string a and b and if they are equal, increment the counter
        if a[i:j] == b[i:j]:
            count += 1
        i+=1
        #return the total count
    return count

print(string_match('xxbaaz', 'xxcaazz'))
