# Structured Exercise
'''Write a program that prints the numbers from 1 to 50.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. '''


#Loop through integers from 1-50
#if number / 3 == 0
#print fizz
#elseif number / 5 == 0
#print buzz
#elseif number /3 == 0 and number /5 == 0
#print fizzBuzz
#else
#print number
starting_no = 1
ending_no = 50
while starting_no <= ending_no:
    if starting_no % 3 == 0 and starting_no % 5 == 0:
         print('fizzbuzz')
    elif starting_no % 3 == 0:
        print('fizz')
    elif starting_no % 5 == 0:
        print('buzz')
    else:
        print(starting_no)
    starting_no+=1