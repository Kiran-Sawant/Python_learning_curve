locations = {0: "You are sitting in front of the computer",
             1: "You are standing in front of the road before a brick building",
             2: "You are at the top of a hill",
             3: "You are inside a buiding",
             4: "You are in a valler besides a stream",
             5: "You are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "E":3, "N":5, "S":4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"W":1, "Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2, "S":1,"Q":0}}

alternative = {"NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W",
               "QUIT": "Q"}

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