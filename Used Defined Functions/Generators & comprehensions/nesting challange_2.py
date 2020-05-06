locations = {0:"You are sitting in front of the computer",
             1:"You are standing in front of the road before a brick building",
             2:"You are at the top of a hill",
             3:"You are inside a buiding",
             4:"You are in a valler besides a stream",
             5:"You are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "E":3, "N":5, "S":4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"W":1, "Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2, "S":1,"Q":0}}

print('Nested for loops')
print("-"*30)
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print(f"Locations leading to {loc}", end='\t')
    print(exits_to_destination_1)

print('\n')

print("List comprehensions inside a for loop")
print('-'*30)
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits]
    print(f"Locations leading to {loc}", end='\t')
    print(exits_to_destination_2)

print('\n')

print("Nested comprehension")
print('-'*30)
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
print(exits_to_destination_3)

print('\n')
for index, loc in enumerate(exits_to_destination_3):
    print(f"Locations leading to {index}", end='\t')
    print(loc)