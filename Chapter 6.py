family_0 = {
    'username': 'tblaze',
    'first_name': 'trevor',
    'last_name': 'blaszczyk'
}
for key, value in family_0.items():
    print("\n Key : " + key)
    print("Value : " + value)

favorite_player = {
    'jimmy': 'Hossa',
    'dad': 'McDavid',
    'banj': 'Kane',
    'pev': 'Mackinnon'
}

best_answer = ['banj','pev']
for name in favorite_player.keys():
    print(name.title())

if name in best_answer:
    print("Howdy " + name.title() +
          ", " + favorite_player[name].title()
          + " is the best player, you're right.")