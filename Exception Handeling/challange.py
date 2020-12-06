"""Write a short program to ask the user two enter two integer numbers,
then print out the first number divided by the second number.
The program shouldn't crash, no matter what the user types in.
(Lost)"""

def getint():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print('Wrong value inserted!, try again..')

no_1 = getint()
no_2 = getint()

try:
    print(f"{no_1} / {no_2} = {no_1/no_2:.2f}")
except ZeroDivisionError:
    print(f"{no_1} cannot be divided by {no_2}")