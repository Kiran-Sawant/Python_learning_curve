"""Learning type annotations line: 65
   Learning to raise custom errors in line: 67~71, 'raise' clause
   Learning isistance method line: 68
   Learning getattr() & callable() on line 66~67"""

class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work but i'm flying")
        else:
            print("I think I'll ust walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)      #composition

    def walk(self):
        print('Waddle, Waddle, Waddle')

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print('Waddle, waddle, I waddle too')

    def swim(self):
        print('Come on in, but its chilly this far south')

    def quack(self):
        print("Are you 'avin' a 'larf'?, I'm a penguin")

    def aviate(self):
        print("I won a lottery and bought a learjet!")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = list()

    def add_duck(self, duck: Duck) -> None:         #Type annotation
        fly_method = getattr(duck, 'fly', None)     #Checks if the object contains the passed argument in '', if not gives error/default value.
        if callable(fly_method):
        # if isinstance(duck, Duck):                #Checks if the argument is an instance of the given class
            self.flock.append(duck)
        else:                                       # raise error if the passed object is not an instance of Duck
            raise TypeError(f"Cannot add duck, are you sure its not a {str(type(duck).__name__)}?")

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                # raise AttributeError("Testing exception handeling.")         # TODO remove before release
            except AttributeError as e:             #Getting a refrence of error in variable e
                print("One duck Down")
                problem = e
        if problem:
            raise problem
                
if __name__ == '__main__':
    donald = Duck()
    donald.fly()