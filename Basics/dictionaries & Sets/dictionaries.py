fruit = {"orange": "A sweet orange citrus fruit",    # dictionary literal
    "apple": "Good for making Cider",                # keys must be unique
    "lemon": "A sour, yellow citrus fruit",
    "grape": "A small, sweet fruit growing in bunches",
    "lime": "A sour, green citrus fruit"}            # "lime" is a key. keys must be immutable objects

print(fruit)                          # Print the dictionary
print(fruit["lime"])                  # print the value of key "lime"

fruit["pear"] = "an odd shaped apple" # incerting a new key-value pair in the dictionary
print(fruit)

fruit["pear"] = "great with tequila"  # updating the values of an existing key
print(fruit)

del fruit["lime"]                     # deleting a key-value pair from a dictionary
print(fruit)

# fruit.clear()                       # clear() method empties the dictionary
# print(fruit)

for key in fruit:                     # an iterator only iterates through the keys & not their values
    print(key)

for key in fruit:                     # iterating through the values of keys & not keys themselves
    print(fruit[key])

input()                               # used to keep the console running, press enter to close.