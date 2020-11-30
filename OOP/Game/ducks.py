"""learning Polymorphism through composition.
Polymorphism through composition is when a class has attributes
that are composed of objects defined by another class.
like on line 24 the _wing attribute of Duck Class is an Object of
Wing class, so therefore Duck has attributes COMPOSED of other class
instances."""

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

    def walk(self):
        print('Waddle, waddle, I waddle too')

    def swim(self):
        print('Come on in, but its chilly this far south')

    def quack(self):
        print("Are you 'avin' a 'larf'?, I'm a penguin")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()