#Movies Tickets

ticket_price = 0
answer = int(input("I understand you want to watch a movie, what is your age?"))

if answer <= 3:
    print(ticket_price)
elif 2 <= answer <= 12:
    ticket_price = 10
else: 
    ticket_price = 15

print("The cost of your ticket is $" + str(ticket_price))
    