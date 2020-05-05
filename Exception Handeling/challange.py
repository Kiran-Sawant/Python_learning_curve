"""Lost"""

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