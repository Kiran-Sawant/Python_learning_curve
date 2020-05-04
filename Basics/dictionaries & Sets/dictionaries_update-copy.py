fruit = {"orange": "A sweet orange citrus fruit",    #dictionary literal
    "apple": "Good for making Cider",                #keys must be unique
    "lemon": "A sour, yellow citrus fruit",
    "grape": "A small, sweet fruit growing in bunches",
    "lime": "A sour, green citrus fruit"} #"lime" is the key, keys must be immutable objects

print(fruit)

veg = {"cabbage": "Every childs Favorite",
       "sprouts": "lovely",
       "spinach": "Popeyes Favorite"}

print(veg)

veg.update(fruit) #adds fruit in veg
print(veg)

print(fruit.update(veg)) #does not return anything
print(fruit)

mix = fruit.copy() #copies fruit in a new veriable
mix.update(veg)
print(mix)