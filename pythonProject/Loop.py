person_list = []
person = ['Tony', 45]
person_list.append(person)

person = ['Steve', 98]
person_list.append(person)

person = ['Stacie', 28]
person_list.append(person)

person = ['Mick', 64]
person_list.append(person)

person = ['Nick', 34]
person_list.append(person)

print(person_list)

total_age = 0.0
#Getting the average
for pl in person_list:
  #  print(pl)
    age = pl[1]
    total_age += age

print(total_age)

#Average of all ages
average_age = total_age/len(person_list)
print(average_age)

#Square all ages and add them into a list
squared_age = []
for pl in person_list:
  age = pl[1]
  sq_age = age * age #Square the age
  squared_age.append(sq_age)

print(squared_age)

#Single line code
squared_age2 = [pl[1] * pl[1] for pl in person_list]
print(squared_age2)

#For loop will do somthing for something in something
#-------------------------------------------------------------------------
#While loop
x = 4
y = 0.0
while x < 10:
  y += x * x
  x += 1

print(y)