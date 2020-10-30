"""A set object in python is an iterable set of unique objects
similar to mathematical sets."""

farm_animals = {"sheep", "cow", "hen"} # set literal
print(farm_animals)

for animals in farm_animals:
    print(animals)

print("=" * 40) #________________#set() constructor method_______________________#

wild_animals = set(["Lion", "tiger", "panter", "elephant", "hare"]) #set() constructor converts passed iterable into a set
print(wild_animals)

farm_animals.add("horse")                       # adding a value to the set
wild_animals.add("horse")                       # adding a value to the set
wild_animals.remove('hare')                     # removing a value, Key error if not present
print(farm_animals, "\n", wild_animals)

empty_set = set()                               # for creating an empty set use set() constructor only

print("=" * 40 + "\nUnion() method:-") #______________union() method_________________#

even = set(range(0, 40, 2))                     #passing a range in a set
print("Even = ", even)

square = (4, 6, 9, 16, 25) #tuple
square_set = set(square)                        #passing a tuple in a set() costructor
print("Square set = ", square_set)

print("Even.union(square set) = ", even.union(square_set)) #.union() method carries an arithmetic union operation on the sets
print("len(Even.union(square set)) = ", len(even.union(square_set))) #length of united sets

print("="*40 + "\nIntersection method:-") #__________intersection() method_______________#

print("Even.intersection(square set) = ", even.intersection(square_set))
print("Even & square set = ", even & square_set) # & works as a intersection operator on sets

print("="*40 + "\n.difference() method:-") #______________difference() method_______________#

print("Even.difference(Square set) = ", even.difference(square_set)) #.difference() method removes the values of iterable passed() from set to which it is applied
print("Even - Square set = ", even - square_set)

# print("="*40) #____________________difference_update method()_________________________#

# even
#.difference_update(square_set) #.difference_update() method removes the values of iterable passed() from set to which it is applied & updates the existing set
# print(sorted(even))

print("="*40 + "\nSymetric difference:-") #____________symmetric_difference() method____________#

print("Symetric even minus square set")
print(even.symmetric_difference(square_set)) #prints all the elements in both sets except the common ones

print("Symetric square set minus even")
print(square_set.symmetric_difference(even)) #prints all the elements in both sets except the common ones

# square_set.discard(4) #removes the passed values from the applied set
# print(square_set)

print("="*40 + "\nFrozen set:-") #________________frozenset() method_______________________#

even100 = frozenset(range(0,100,2)) # Creates an immutable set even100
print("even100 = ", even100)