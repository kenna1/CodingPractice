values = [7, 12, 8, 3, 40]

# Find the highest number in the list

highestVal = values[0]

for v in values:
    if v > highestVal:
        highestVal = v

print (highestVal)