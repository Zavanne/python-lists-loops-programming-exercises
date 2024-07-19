all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here

def names_with_r (name):
     return name[0].lower() == 'r'

resulting_names = list(filter(names_with_r, all_names))

print(resulting_names)

def names_with_rr (name):
     return name[0].lower() == 'r'

resulting_names_two = list(filter(lambda name:  name[0].lower() == 'r', all_names))

print(resulting_names_two)

resulting_names_three = [name for name in all_names if name[0].lower() == 'r']

print(resulting_names_three)




