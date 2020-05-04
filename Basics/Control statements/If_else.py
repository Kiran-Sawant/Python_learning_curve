name = str(input("Please type your name: "))
age = int(input("How old are you {0}?".format(name)))

if age >= 18:
    print("You're old enough to vote")
    print("Go get a job fool!!")
else: # age is less than 18 years
    print("Please come back in {0} years".format(18 - age))

print("="*50) #Separator#######################################

print("Please guess a number between 0 & 10")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Guess higher!")
    else: #guess > 5
        print("Guess lower!")
    guess = int(input())
    if guess == 5:
        print("Well done {0}!, you got it right".format(name))
    else:
        print("You loose!")
else:
    print("You got it right the first time {0}!".format(name))