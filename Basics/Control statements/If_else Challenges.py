"""Write a small program to ask for name & age.
when the values are entered check if the person is the
right age to go for a 18~30 holiday, they must be over 18
and under 31."""

name = str(input("Enter your name: "))
age = int(input("What's your age {0}? ".format(name)))

if (age > 18) and (age <=30):
    print("Welcome to the holiday {0}!".format(name))
elif age <= 18:
    print("you are too young dickhead! try after {0} years...\U0001F595".format(19 - age))
else: # age > 30
    print("Fuck OFF!!, Boomer!")