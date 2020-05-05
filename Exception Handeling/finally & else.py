import sys

def getint():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except EOFError:
            sys.exit(1)
        except: #wildcard exception excepts everything [ValueError]
            print('Wrong value inserted!, try again..')
        finally:                                            #finally is always executed whether exception or not
            print("Finally always executes")

no_1 = getint()
no_2 = getint()

try:
    print(f"{no_1} / {no_2} = {no_1/no_2:.2f}")
except ZeroDivisionError:
    print(f"{no_1} cannot be divided by {no_2}")
    sys.exit(2)
else:                                                       #else is executed after the try block is successful & exception was not raised
    print("Division was successful!")