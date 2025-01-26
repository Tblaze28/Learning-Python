#While Loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\n Tell me something you would like repeated."
prompt += "\n Enter 'quit' to shut me up."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)