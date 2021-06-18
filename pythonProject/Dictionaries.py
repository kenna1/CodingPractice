'''team = {"Tony": "Robotics", "Bruce": "Science", "Thor": "Electrics", "Steve": "Management", "Natasha": "Intelligence", "Clint": "Vision", "Wanda": "Mindfulness"}

team_b = team
team_c = team.copy()

#team_b['Thor'] = 'Thunder Hammer'
#team['Thor']
#print(team.pop("Robotics"))
#print(team.popitem())
#team_c['Thor'] = 'God of Glorious Hair'
#team['Thor']
#print(team_c)

print(team.items())
print(team.keys())
print(team.values())'''

#Guided Activity
team = {"Tony": "Robotics", " Bruce": "Science", "Thor": "Electrics", "Steve": "Management", "Natasha": "Intelligence", "Clint": "Vision", "Wanda": "Mindfulness"}
'''team_b = {}
team_b = dict((team.popitem()))
team_b = dict((team.popitem()))
team_b = dict((team.popitem()))'''

team_b = dict([team.popitem(),team.popitem(),team.popitem()])

print(team_b)

len_str_team_a =  str(team)
len_str_team_b = str(team_b)

print(len(len_str_team_a))
print(len(len_str_team_b))