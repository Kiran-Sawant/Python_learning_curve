i = 1         # While loop needs initialization of the variable
while i < 10: # While loop performs iteration on the basis of logical condition applied on the pre defined variable
    print("i is now {0}".format(i))
    i += 1    # Augmented assignment

print("="*20 + "Direction Game\n") #_________Direction Game____________#

exits = ["east", "north east", "south"]

chosenExit = "" # Variable Initialization
while chosenExit not in exits:
    chosenExit = input("please choose any direction: ")
    if chosenExit == "quit":
        print("Good bye!")
        break
else:
    print("You got out of the shit hole!")