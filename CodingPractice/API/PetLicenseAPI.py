from urllib.request import urlopen

url = 'https://data.seattle.gov/resource/jguv-t9rb.csv'

response = urlopen(url)

data = response.read()

# Converting it to a stringA
data = data.decode()

print(type(data))

file_name = 'C:/Users/ikenn/PycharmProjects/pythonProject/petlicenses.csv'
f = open(file_name, 'w')
f.write(data)
f.close()
response.close()
#print(data)