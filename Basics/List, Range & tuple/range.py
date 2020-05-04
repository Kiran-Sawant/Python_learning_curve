decimals = range(0, 100) #range is not a list
print(decimals)

my_range = decimals[3:40:3] #describes a range within another range from 3 to 39 with a step of 3
print(my_range)

for i in my_range:
    print(i)

print("=" * 50)

for i in range(3, 40, 3): #does the same thing as line 7.
    print(i)
    
print("="*50)

#range is not a list but can be used to make one
listx = list(my_range)
print(listx)

#Range with negative step
Rstring = "egaugnal lufrewop a si nohtyP"
print(Rstring[::-1]) #A range with a negative step starts from backwards ie.RHS

for i in range(10, 0, -1): #while defining a range with negative step mind the start & end points
    print(i)