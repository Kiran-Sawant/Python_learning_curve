car = ["Ferrari", "Fiat", "Chrysler", "Tesla"] #Creating lists using [] with values separated by ,
car.append("Jaguar") #adding new value in the end of an existing list
car = car[:2] + ["Toyota"] + car[2:] #adding value in the middle of the list

for i in car:
    print("We have "+ i +"s")

car.remove('Fiat') #list.remove() deletes the first occurrence passed value, raises a valueError if not found

#______Sorting values inside the list______#
even = [0, 2, 4, 6]
odd = [1, 3, 5, 7,]

num = even + odd                      # creating new unsorted list by adding two previous lists.
print(f"num: {num}")

num_sort = sorted(num)                # sorted() function is used to create a new ordered list.
#num_sort = sorted(num, reverse=True) # reverse parameter sorts in decending order if set to True.
print(f'sorted_num: {num_sort}')

num.sort()                            # list.sort() method modifies the original list in memory.
print(f'num.sort(): {num}')
#_____________list() constructer_________#
k = list(range(1, 50, 2)) #list() constructor creates a list with the given parameters & assigns it to the variable
print(k)

#_____________Nested list Operations___________#

car2 = ['Lamborghini', 'Saab', 'MG']
car3 = ['Dodge', 'Chevrolet', 'Ford']
car2.append(car3) #appending car3 to car2
car.append(car2)  #appending car2 to car
print(car[6][3][2]) #retriving values inside a list in a list