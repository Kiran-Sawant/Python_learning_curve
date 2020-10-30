for i in range(1, 20): #i stands for index
    print("i is now {}".format(i))
    
print("="*50) #separator

number = "9,223,327,036"
print(number)
strNumber = ''
for i in range(len(number)):
    if number[i] in "0123456789":
        #print(number[i], end = ' ')
        strNumber = strNumber + number[i]
intNumber = int(strNumber)
print("the number is {}".format(intNumber))

print("="*50) #________loops with lists_____________#

for state in ["not pinin", "no more", "a stiff", "bereft of life", "Horny"]:
    print("My parrot is", state)

print("="*50 + "\n Range Function") #_________nested loops__________#

for i in range(1, 11):
    for j in range(1, 11):
        print("{0} times {1:2} is {2:3}".format(i, j, i * j))
    print("="*20)

print("="*50 + "Continue function\n") #_________Continue & Break Function____________#

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
nasty = ""

for item in shopping_list:
    if item == "spam":
        print("Fuck {}!".format(item))
        continue #continue bypasses the code block ahead in the loop and goes back to the loop for new value
    print("buy {}".format(item))

print("="*20, 'Break function') #separator

for item in shopping_list:
    if item == "spam":
        nasty = item
        break # break terminates the loop entirely
    print("I'll have a plate of {}, then, place".format(item))
print("Can I have anything without {} in it".format(nasty))

print("="*20 + "Augmented Assignment") #____________Augmented Assignment_____________#

number = "9,223,327,036"
print(number)
strNumber = ''
for i in range(len(number)):
    if number[i] in "0123456789":
        #print(number[i], end = ' ')
        #strNumber = strNumber + number[i]
        strNumber += number[i] # += is an augmented assignment does the same thing as line 56 but more efficiently
intNumber = int(strNumber)
print("the number is {}".format(intNumber))