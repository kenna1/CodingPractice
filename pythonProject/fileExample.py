filename = '/Users/ikenn/Desktop/Python_Resources_Folder/Seattle_Pet_Ownership_Data.csv'

f = open(filename,'r')

data = f.read()

data = data.split("\n")

#print(type(data))
print(data[0])
print()
#print(data[-3:])
data.pop()
#print(data[-3])
headers = data[0].split(',')
row = data[1].split(',')
print(data[0].split(','))
print()
zip(headers, row) # This sticks two lists together
row_dict = dict(zip(headers,row))
#print(row_dict)
output_file_name = '/Users/ikenn/Desktop/Python_Resources_Folder/reduced_police_data.csv'
fo = open(output_file_name, 'w')
#print(fo)

for d in data:
    row = d.split(',')
    row_dict = dict(zip(headers,row))
    out_str = row_dict['license_issue_date'] + ',' + row_dict['license_number'] + ',' + row_dict['zip_code'] + '\n'
    fo.write(out_str)

f.close()
fo.close()

f = open(output_file_name, 'r')
data = f.read()
data = data.split('\n')
print(data[:3])
f.close()

'''#you will need to change to file_name to where Seattle_Police_Department_Police_Report_Incident.csv is located

file_name = '/Users/[Name]/Downloads/Seattle_Police_Department_Police_Report_Incident.csv'

f = open(file_name, 'r')

data = f.read()

data = data.split('\n')

data[3][:10]'''