jab = open("sample.txt", mode='r') #open built-in function opens a text file passed in the ()
                                   #mode can be read(r) or write(w)

for line in jab:
    print(line, end="") #end="" prevents starting a new line after finishing the line, '\n' is its default value

jab.close() #not closing the file after reading it ccan corrupt it.

print("\n\n"+ "="*10 + "with statement"+ "="*10)#__________With Statement______________#

with open("sample.txt", mode='r') as jabber: #with handels the file in a separate code block as the program xits the block the file is automatically closed
    for line in jabber:
        if 'jab' in line.lower():
            print(line, end="")

print("\n\n" + "="*50) #_________________readline() method_______________#

with open("sample.txt", mode='r') as jab:
    lines = jab.readline() #readline() passes only one line @ a time
    while lines:
        print(lines, end='')
        lines = jab.readline() #here readline() goes to the next line in the file & assigns it to lines

print("\n\n"+ "="*20+"In reversed order"+ "="*10)#______________readlines() method______________________#

with open("sample.txt", mode='r') as jab:
    lines = jab.readlines() #readlines() reads all the lines in the file & stores them in a list of strings
#print(lines) # here lines is a list

for line in lines[::-1]: #iterates through list lines in reverse order
    print(line, end='')  #prints objects in list lines in reverse

print("\n\n"+ "="*20+"In reversed alphabetical order"+ "="*10)#____________read() method_________________#

with open("sample.txt", mode='r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')