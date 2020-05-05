cities = ["Mumbai", "Delhi", "Bangalore", "Hydrabad", "Tiruvananthapuram"]

with open("cities.txt", mode='w') as cityFile:
    for city in cities:
        print(city, file=cityFile) #Writing to our file

print("="*50)#________________reading our file_________________________#

cities = []

with open("cities.txt", mode='r') as cityFile:
    for city in cityFile:
        cities.append(city.strip('\n')) #strip() function moves the passed string fron the start & end of the retrived string
for i in cities:
    print(i)

print("="*50)#________________eval() function_________________________#

imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the rug"),
         (2, "Psyco"), (3, "Mayhem"), (4, "Kentish town walt"))

with open("imelda.txt", mode='w') as imeldaFile: #creating the file
    print(imelda, file=imeldaFile) # writing to file

#______________reading our file________________#
with open("imelda.txt", mode='r') as imeldaFile2:
    contents = imeldaFile2.readline()

imelda = eval(contents) #eval() function evaluates the text line to determine which built-in object type it is & assigns it to the variable
Album, Artist, year, tracks = imelda #unpacking the tuple
print(Album)
print(Artist)
print(year)
print(tracks)