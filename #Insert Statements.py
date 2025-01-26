#IF Statements

#name = input("\nWhat is your name?!   ")
#print("Howdy " + name + "!")

prompt = ("Tell me a little about yourself and I'll repeat it back.")
prompt += "\n What is your name?"

#retrieving info
name = input(prompt)
print("\nHowdy, " + name)
age = input("\nHow old are you?\t")
age = int(age)
if age >= 18:
    print("\tYou're old enough to vote!"),
else:
    print("\tYou're too young to vote!")
height = input("\nHow tall are you? (in inches)\t")
height = int(height)
if height >= 70:
    print("\tWoah, do you play basketball?")
else:
    print("\tShort fella are you?")
number = input("What is your favorite number?")
number = int(number)
if number % 2 ==0:
    print("ah, divisible by 2, nice, clean number."),
else:
    print("An uglier number, but to each their own.")