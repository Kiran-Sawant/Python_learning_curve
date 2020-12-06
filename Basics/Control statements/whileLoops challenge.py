"""Modify the program such that it allows the user to make
as many guesses as he wants, if the guess is lower than the
number prompt user to guess higher and vice-versa."""

import random

print("="*20 + "Random number Game\n") #_________Random number Game____________#

highest = 10
answer = random.randint(1, highest) #Returns random int between the given range including the end numbers

print("Guess a number between 1 and {} or press 0 to quit: ".format(highest))
guess = 0
#________code block to be modified__________#
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
        print("bye, bye!")
        break
    if guess < answer:
        print("Please guess a little higher")
    elif guess > answer:
        print("Please guess a little lower")
    else:
        print("Good! you guessed it right")