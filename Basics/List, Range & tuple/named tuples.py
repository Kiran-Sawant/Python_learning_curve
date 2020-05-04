from collections import namedtuple

#___________Creating named tuple object________________#
Colour = namedtuple('RGB_levels',['red', 'green', 'blue']) #RGB_levels is the defination of what the tuple contains
                                                           #the red, green & blue are the headers for making named tuples
#_______Creating named tuples_________#
colour = Colour(25, 55, 65)
colour2 = Colour(23, 56, 98)

print(colour)
print(colour2.red) # retriving the specific tuple value by passing tuple name