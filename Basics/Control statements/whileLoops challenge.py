import random

print("="*20 + "Random number Game\n") #_________Random number Game____________#

highest = 10
answer = random.randint(1, highest) #Returns random int between the given range including the end numbers

print("Guess a number between 1 and {} or press 0 to quit: ".format(highest))
guess = 0
# if guess != answer:
#     if guess < answer:
#         print("Guess a little higher")
#     else:
#         print("Guess a little lower")
#     guess = int(input())
#     if guess == answer:
#         print("You win")
#     else:
#         print("You have not guessed correctly")
# else:
#     print("Good!, you guessed it right the first time.")

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("by, by!")
        break
    if guess < answer:
        print("Please guess a little higher")
    elif guess > answer:
        print("Please guess a little lower")
    else:
        print("Good! you guessed it right")