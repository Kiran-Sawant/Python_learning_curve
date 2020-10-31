cities = ["Mumbai", "Delhi", "Bangalore", "Hydrabad", "Tiruvananthapuram"]

with open("cities.txt", mode='w') as cityFile:
    for city in cities:
        print(city, file=cityFile) #Writing to our file

print("="*50)#________________reading our file_________________________#

cities = []

with open("cities.txt", mode='r') as cityFile:
    for city in cityFile:
        cities.append(city.strip('\n')) # strip() method removes the passed string from the start & end of the retrived string.
for i in cities:
    print(i)

print("="*50)#________________eval() function_________________________#

imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the rug"),
         (2, "Psyco"), (3, "Mayhem"), (4, "Kentish town walt"))

with open("imelda.txt", mode='w') as imeldaFile: # creating the file
    print(imelda, file=imeldaFile)               # writing to file

# reading our file
with open("imelda.txt", mode='r') as imeldaFile2:
    contents = imeldaFile2.readline()

"""eval() function evaluates the text line to determine which python built-in object type it is & assigns it to the variable.
In this case the text resembles a tuple, therefore imelda will be a tuple."""

imelda = eval(contents)
Album, Artist, year, tracks = imelda # unpacking the tuple
print(Album)
print(Artist)
print(year)
print(tracks)