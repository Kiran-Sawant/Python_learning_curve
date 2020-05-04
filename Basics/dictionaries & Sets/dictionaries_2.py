fruit = {"orange": "A sweet orange citrus fruit",    #dictionary literal
    "apple": "Good for making Cider",                #keys must be unique
    "lemon": "A sour, yellow citrus fruit",
    "grape": "A small, sweet fruit growing in bunches",
    "lime": "A sour, green citrus fruit"} #"lime" is the key, keys must be immutable objects

ordered_keys = list(fruit.keys()) #keys() method retrives the keys from the dictionaries
ordered_keys.sort()
for f in ordered_keys:
    print(f + "-" + fruit[f])

print("="*50) #separator

for f in sorted(fruit.keys()): #does the same thing as line 7~10
    print(f +" - " + fruit[f])

print("="*50) #separator

for v in fruit.values(): #values() method retrives the values in dictionary
    print(v)

print("="*50) #separator

for key in fruit: #does the same thing as line 19 ~ 20
    print(fruit[key])

input()
