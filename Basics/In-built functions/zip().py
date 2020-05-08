lst1 = [1, 2, 3, 4, 5, 6]
tup = ('Killer', 'Bean', 'Forever', 'Tommy', 'Vercetti')
set1 = {'@', '#', '$', '%', '^', '&'}

k = zip(lst1, set1, tup)    #creating a zip() object

print(list(k))              #creating a list out of zip

print(tuple(zip(lst1, set1, tup)))      #creating a tuple out of zip

# s = dict(k)               #doesnot work
s = dict(zip(lst1, set1))
print(s)
