class Kettle(object):

    #Creating class attributes
    power_source = 'Electricity'
    print(f"Dict of global variables to Kettle: {globals()}\n")
    print(f"Dict of local variables to Kettle: {locals()}\n")
    #creating a constructor method
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.switch = False
        print(f"Dict of global variables to Kettle.__init__: {globals()}\n")
        print(f"Dict of local variables to Kettle.__init__: {locals()}\n")
    #Creating a method
    def switch_on(self):
        self.switch = True

k = 258
kj = "Killer Bean Forever"
j = Kettle('Wellington', 200)

print(f"Dict of local variables to module: {locals()}\n")
print(f"Dict of global variables to module: {globals()}\n")