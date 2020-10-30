myList = ["a", "b", "c", "d"]
newString = ", ".join(myList) # join() method creates a string with the values passed in it, delimited by the applied string.
print(newString) 

splitString = newString.split(", ") #split is the opposit of join, creates a list of all objects with a delimiter between them
print(splitString)