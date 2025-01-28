#While Loop
#current_number = 1
#while current_number <= 5:
    #print(current_number)
    #current_number += 1

##prompt = "\n Tell me something you would like repeated."
#prompt += "\n Enter 'quit' to shut me up.\t"
#message = ""
#while message != 'quit':
    #message = input(prompt)

    #if message != 'quit':
        #print(message)

#Input City Loop
prompt = "\n Enter the name of a city you've been to!"
prompt += "\n'quit' to stop\t"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + " someday!")

#counting loop skipping numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue

    print(current_number)

#counting Loop
x = 1
while x <5:
    print(x)
    x += 1