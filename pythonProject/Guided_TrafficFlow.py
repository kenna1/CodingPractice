from urllib.request import urlopen

new_url = 'https://data.seattle.gov/resource/xw6n-ahw3.csv'

#Open the link in python using urlopen
response = urlopen(new_url)

# Reading the response
data = response.read()

#Converting the data returned into a string
data = data.decode()

filename = 'C:/Users/ikenn/PycharmProjects/pythonProject/datastore'

fo = open(filename, 'w')
fo.write(data)
fo.close()

#-------------------------------------------------------------------------------------------------

f = open(filename, 'r')
lines = f.read()
lines = lines.split('\n')
lines.pop()
print(lines)

'''
print(lines[1])
print()
endChar = []
endChar = lines[1].split(",")
lastWord = endChar.pop()
print(len(lastWord))
#print(lines[2])'''
f.close()

#--------------------------------------------------------------------------------------------------
#Guided Activity 2