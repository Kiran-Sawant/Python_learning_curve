from datetime import datetime as dt

#_____example 1_____#
firstName = 'Kiran'
lastName = 'Sawant'

sentence = "My name is {0} {1}".format(firstName, lastName)         #normal formating
fSentence = f"My name is {firstName.upper()} {lastName.upper()}"    #F-String formating

#_____example 2_____#
person = {'name': 'Jenn', 'age': 24}

sentence2 = f"My name is {person['name']} and I am {person['age']} years old"

#_____example 3_____#
calculation = f"4 times 11 is equal to {4*11}"

#_____example 4_____#
for i in range(1, 11):
    sentence3 = f"The value is {i:>2}"

#_____example 5_____#
pi = 3.14159265

sentence4 = f"Pi is equal to {pi:.4f}"  #.4f means a prision of 4 digits after decimal(roundoff)

#_____example 6_______#
birthday = dt(1990, 1, 2)

sentence5 = f'Jenn has a birthday on {birthday: %B %d, %Y}' #objects passed in the {} can be formated in the {} using :
print(sentence5)