result = "Manchester United:2,Arsenal:1"
#pseudo code
# print Home team : Manchester ":" "2" "," Arsenal, ":1"

#Split at colon
new_result = result.split(":")
#Split the new_result list at comma
arsenal_split= new_result[1].split(",")

#print(new_result)
#print(arsenal_split)
#Print format
print("Home Team:"+new_result[0]+" - "+"Score:"+ arsenal_split[0])
print("Away Team:"+arsenal_split[1]+" - "+"Score:"+ new_result[2])

''' Alternative solution using format
Solution
results = "Manchester United:2,Arsenal:1" 

teams = results.split(',')

team1 = teams[0].split(':')

team2 = teams[1].split(':')

result = """Home Team: {} - Score: {} \n 

Away Team: {} - Score: {}""".format(team1[0],team1[1],team2[0], team2[1])

print(result)
'''