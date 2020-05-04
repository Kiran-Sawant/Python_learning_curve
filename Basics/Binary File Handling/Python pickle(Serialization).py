import pickle # importing pickle module

imelda = ("More Mayhem",
        "Imilda May", 
        2011, 
        ((1, "Pulling the rug"), 
        (2, "Psyco"), 
        (3, "Kentish town Waltz"), 
        (4, "Mayhem"))) #Creating an object for pickling

#__________________Creating a pickle file__________________#

with open('imelda.pickle', mode='wb') as pickleFile: #Creating a pickle file and assigning it to pickleFile var
    pickle.dump(imelda, pickleFile) #pickle.dump() writes the passed object into passed variable

#__________________Reading a pickle file____________________#

with open('imelda.pickle', mode='rb') as imeldaPickle: #reading a pickle file & pasting the content in imeldaPickle var
        imeldaObject = pickle.load(imeldaPickle) #pickle.load() assigns the object in the pickle var to the var

album, artist, year, tracks = imeldaObject #unpacking tuple
print('Album: ' + album)
print('Artist: '+ artist)
print('year: ', year)
for track in tracks:
        track_no, track_name = track #Unpacking tuple in a loop
        print(track_no, ': '+ track_name)

#______________________________________Pickling Multiple Objects_______________________________________#

even = list(range(0, 10, 2)) #New Objects
odd = list(range(1, 10, 2))  #

#______________dumping to pickle file______________#
with open('imelda.pickle', mode='wb') as pickleFile: #Overwriting a previously created pickle
        pickle.dump(imelda, pickleFile, protocol=0)  #dumping objects to a pickle file
        pickle.dump(even, pickleFile, protocol=1)    #protocol= is used to assign a protocol to the dumping
        pickle.dump(odd, pickleFile, protocol=pickle.DEFAULT_PROTOCOL) #another way of assigning a protocol
        pickle.dump(2998302, pickleFile, protocol=pickle.HIGHEST_PROTOCOL)

#______________reading a pickle file________________#
with open('imelda.pickle', mode='rb') as imeldaPickle:
        imeldaTuple = pickle.load(imeldaPickle) #load() must be in the same order as dump()
        even_list = pickle.load(imeldaPickle)
        odd_list = pickle.load(imeldaPickle)
        x = pickle.load(imeldaPickle)

album, artist, year, tracks = imeldaTuple #unpacking tuple
print('Album: ' + album)
print('Artist: '+ artist)
print('year: ', year)
for track in tracks:
        track_no, track_name = track #Unpacking tuple in a loop
        print(track_no, ': '+ track_name)

print('='*50) #Separator

for i in even_list:
        print(i)

print('='*50) #Separator

for i in odd_list:
        print(i)

print('='*50) #Separator

print(x)

print('='*50) #Separator

# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR)") #Used to delete the pickle file in the directory