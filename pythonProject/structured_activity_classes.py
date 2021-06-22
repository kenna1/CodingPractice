#Convert the integers into roman numerals
''' 10, 532, 4678, 1992 '''

#Define the class
#Initialiser

int_num = []
#int_num = [[10, 'X'], [532, 'DXXXII'], [1992, 'MCMXCII'], [4678, "MMMMDCLXXVIII"]]
int_num = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'],[ 1, 'I']]



def toRoman(num):
    i = 0
    output = ""
    while num > 0:
        while int_num[i][0] > num:
            i+=1
        output += int_num[i][1]
        num -= int_num[i][0]

    return output

print (toRoman(4678))


#------------------------------------------------------------------------
'''int_num = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],

         [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],

         [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],

         [   1, 'I']]

def int_to_roman_numeral(number):

    i = 0

    output = ''

    while number > 0:

        while int_num[i][0] > number: 

            i+=1 #increments i to largest value greater than current number

        output += int_num[i][1] #adds the roman numeral equivalent to string

        number -= int_num[i][0] #decrements number

    return output

print('10 Converted to Roman Numerals ' + int_to_roman_numeral(10))

print('532 Converted to Roman Numerals ' + int_to_roman_numeral(532))

print('4678 Converted to Roman Numerals ' + int_to_roman_numeral(4678))

print('1992 Converted to Roman Numerals ' + int_to_roman_numeral(1992))'''