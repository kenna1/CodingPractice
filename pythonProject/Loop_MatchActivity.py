x = 1
y = 1
s = ''
while x <= 3:
    y+=1
    x+=1
    if x > 2:
        s+='_sky'
    else:
        s+='sky'
#print('Hello'+''+s)

#-------------------------------------------------------------------------------------------------------------------
employees = {'Nick':38,'James':37,'Manuel':58,'Ryan':21,'Biz':20}
names = []
ages = []
b = 0
for i in employees:
    names.append(i)
    #names.append(employees)
    ages.append(employees[i])
    #print(type(names[b]))
    b+=1
#print(names)
#print(ages)
print()

#Question 3----------------------------------------------------------------------------------------------------------
total_characters = 0
for t in names:
    print(len(t))
    total_characters += len(t)

print(len(str(names)))