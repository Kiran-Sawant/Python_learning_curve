import shelve #importing shelve module

#___________________Shelve literal_______________________#
fruit = shelve.open('ShelfTest')                 # Creating a Shelve object.
fruit['Orange'] = "a sweet, orange, pulpy fruit" # Updating an object with key['Orange']
fruit['Strawberry'] = "Sweet, bright red fruit"  # adding a new object with a new key[] to the shelve

print(fruit['Orange'])
print(fruit['Strawberry'])
# fruit.close() #Closing shelve

#________________Creating shelve using 'with' context manager_____________#
# with shelve.open('ShelfTest') as fruit:               # creating a shelve file with db name as ShelfTest assigned to var fruit
#     fruit['Orange'] = "a sweet, orange, citrus fruit" # assigning objects with keys[] in shelve
#     fruit['apple'] = "Good for making cider"          # shelve keys must be unique strings
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"

#     print(fruit['lemon'])                             # Retriving the objects in shelve by passing their keys[]
#     print(fruit['apple'])

# print(fruit)                                          # Prints shelves memory location

#_______retriving shelve values on input________#
while True:
    shelfKey = input("Please enter a fruit: ")
    if shelfKey == 0:
        break

    description = fruit.get(shelfKey, "We don't have a " + shelfKey) # .get() retrives the object in the shelve with the passed key
    print(description)                                               # .get(key, default) default string is passed if the key is not found
fruit.close()