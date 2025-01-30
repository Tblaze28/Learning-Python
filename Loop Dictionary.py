# loops w/ dictionaries
unconfirmed_users = ['Reilly', 'Jimmy', 'Sissy', 'Banj', 'Pev']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

while 'Pev' in confirmed_users:
    confirmed_users.remove('Pev')

print(confirmed_users)