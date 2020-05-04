import shelve

gameData = shelve.open('gameData')
locations = gameData['locations']
exits = gameData['exits']
alternative = gameData['alternative']


loc = 1 #default location
while True:
    print(locations[loc]) 

    availableExits = ", ".join(exits[loc].keys())

    if loc == 0: #if location is 0 loop will stop
        break

    directions = input("Available directionss are: " + availableExits + " ").upper()
    print()

    #_______________My Solution_____________________#
    # if directions in exits[loc]:
    #     loc = exits[loc][directions] #replacing the old value of loc with a value of a key in a dictionary in a list
    # elif directions not in exits[loc]:
    #     loc = exits[loc][alternative[directions]]
    # else:
    #     print("You cannot go in that direction")

    #_____________Tim's Solution_____________________#
    if len(directions) > 1:
        for word in alternative:
            if word in directions:
                directions = alternative[word]
    
    if directions in exits[loc]:
        loc = exits[loc][directions]
    else: print("You can't go in that direction")

gameData.close()