class Kettle(object):

    #Creating class attributes
    power_source = 'Electricity'
    #creating a constructor method
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.switch = False
    #Creating a method
    def switch_on(self):
        self.switch = True

#_______________dir()________________#
"""The dir() function returns all properties and methods
    of the specified object, without the values, including
    the built-in properties."""

print(f"\nKettle dir: {dir(Kettle)}\n")

#_____________vars()____________#
"""The vars() function returns the __dic__ attribute of an object.
    The __dict__ attribute is a dictionary containing the object's
    changeable attributes."""

print(f"Kettle vars: {vars(Kettle)}")

k = Kettle('Kenwood', 5000)             #Making a kettle object

#_____________getattr() & setattr()_____________#
"""The getattr() function returns the value of the specified
    attribute from the specified object. returns default parameter
    if specified attribute doesn't exist.
    The setattr() function sets the value of the specified attribute of the specified object.
    Syntax: getattr(object, attribute, default)
            setattr(object, attribute, value)"""

j = getattr(k, 'price', 'Not there')
print(f"\ngetattr(k, 'price', 'Not there'): {j}")

m = setattr(k, 'price', 2000)       #setting the price of k
print(f"Resetted price: {k.price}")

#_____________delattr()______________#
"""The delattr() function will delete the specified attribute
    from the specified object.
    Syntax: delattr(object, attribute)"""

# delattr(k, 'price')                   #Deletes the price variable from k
# print(f"k.price: {k.price}\n")

#_____________hasattr()_______________#

print(f"hasattr(k, 'switch_on'): {hasattr(k, 'switch_on')}\n")

#_________________id()________________#
"""The id() function returns a unique id for the specified object.
    All objects in Python has its own unique id.
    The id is assigned to the object when it is created.
    The id is the object's memory address, and will be different for each time
    you run the program."""

print(f"id(k): {id(k)}\n")

#____________isinstance()______________#
"""The isinstance() function returns True if the specified object
    is of the specified type, otherwise False."""

print(f"isinstance(k, type(k)): {isinstance(k, type(k))}")
print(f"isinstance(10, int): {isinstance(10, int)}\n")

#_____________issubclass()______________#
"""The issubclass() function returns True if the specified object
    is a subclass of the specified object, otherwise False.
    Syntax: issubclass(object, subclass)"""

class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)
print(f"is myObj a subclass of myAge?: {x}")
