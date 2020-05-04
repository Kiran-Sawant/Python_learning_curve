# age = int(input("Type your age: "))
# print("Your age is "+age+" years.") #an integer doesnot concatinate with a string

#str() method
age = int(input("Type your age: "))
print("Your age is "+str(age)+" years.") #str() method converts any object to a string.

#Replacement Fields
print("Your age is {0} years.".format(age)) #{n} must be inside & .format() must be outside the string

print('''January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}'''.format(28,30,31)) #{n} in the string refers to n+1th object in .format sequence

for i in range(1, 11): #the range will be from 1 to 10
    print("The number {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2,i**3)) #{:<n} takes n number of spaces in the string & starts on LHS