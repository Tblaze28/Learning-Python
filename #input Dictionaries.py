#input Dictionaries
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name trooper?")
    response = input("Why do you want to serve your country?")

    responses[name] = response

    repeat = input("Is there anyone else who'd like to serve? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n----A List of People Who Want to Serve AND Why----")
for name, response in responses.items():
    print(name + "\t Their reason for wanting to serve is: " + response)