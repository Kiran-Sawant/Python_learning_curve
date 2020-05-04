t = "a", "b", "c" # tuples literal
print(t)

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "NightFlight", "Budgie", 1981
metallica = "Ride the Lightning", "Metallica", 1984
imelda = "More Mayhem", "Imilda May", 2011, ((1, "Pulling the rug"), (2, "Psyco"), (3, "Kentish town Waltz"), (4, "Mayhem")) # nested tuple

print(metallica)
print(metallica[0]) #printing the first element of the tuple  

title, artist, year, track = imelda # unpacking of a tuple
print("title: {0}".format(title))
print("artist: {0}".format(artist))
print("release year: {0}\nSongs".format(year))
for song in track:
    track, title = song #assignment in a different namespace
    print("\t{0}. {1}".format(track, title))

a, b = 12, 13 # assigning values to multiple variables using tuples
print(a)
print(b)
