"""
Class: Template for creating objects, All objects created using the same class will have same charecteristics.
Object: An instance of a class.
Instantiate: Creating an instance of a class.
Method: A function defined in a class.
Attribute: A variable bound to an instance of a class."""

#________Creating a class defination________#
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

#_______creating class instances(Instantiating)_______#
kenwood = Kettle('kenwood', 30)
hamilton = Kettle('hamilton', 25)

#___________calling instance variable___________#
print('Models: {0}: {1}\n{2:>16}: {3}'.format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print('\nModels: {0.make}: {0.price}\n{1.make:>16}: {1.price}'.format(kenwood, hamilton))

#_____Using methods______#
print(hamilton.switch)
hamilton.switch_on()     #using method
print(hamilton.switch)

Kettle.switch_on(kenwood)#another way of using methods
print('\n', kenwood.switch)

#____using class attributes_____#
print('kenwood Power: ', kenwood.power_source)
kenwood.power_source = 'Atomic'
print('new kenwood Power: ', kenwood.power_source)

print('hamilton Power: ', hamilton.power_source)