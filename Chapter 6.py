family = {
    'tblaze': {
        'username': 'tblaze',
        'first_name': 'trevor',
        'last_name': 'blaszczyk',
    },
    'jblaze0': {
        'user_id': 'jimblaze',
        'password': 'Strike3!'
    }
}
for key, value in family.items():
    print("\n User : " + str(key))
    print("Account Info : " + str(value))

favorite_player = {
    'jimmy': 'Hossa',
    'dad': 'McDavid',
    'banj': 'Kane',
    'pev': 'Mackinnon'
}

best_answer = ['banj','pev']
for name in favorite_player.keys():
    print(name.title())

for name in best_answer:
    print("Howdy " + name.title() +
          ", " + favorite_player[name].title()
          + " is the best player, you're right.")
    
if 'jimmy' not in best_answer:
    print("Jimmy, your player stinks.")