string = "This line has\nbreaks several\ntimes" #\n breaks the line and starts the string from a new line
string2 = "This line\thas tabs" #\t adds tabed spaces
print(string,'\n' ,string2)

#Sequence Operations
string3 = "Killer Bean Forever"
print(string3[:6],'\n', string3[7:11],'\n', string3[12:19]) #[:n] selects string objects from 0 to n-1, ie 0 to 5.
                                                            #[7:11] selects string objects from 7 to 10