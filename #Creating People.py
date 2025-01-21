#Creating People
people = []

#Create 15 people
for people_number in range(15):
    new_person = {'look': 'ugly' , 'size': 'fat' , 'height': 'tall' , 'points': '15'}
    people.append(new_person)

#Modify first 3 people
for person in people[0:3]:
    if person['size'] == 'fat':
        person['look'] = 'good'
        person['points'] = '10'
        
#List first 5 people
for person in people[0:5]:
    print(person)

#Show how many peoples
print("The total number of people comes to...\t" + str(len(people)))