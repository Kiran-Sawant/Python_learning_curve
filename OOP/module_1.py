""" The __name__ is an in-built variable that exists in the in-built
scope. __name__ is assigned implicitly to every module by python.
If the module is the initiator module it is given a name '__main__',
if not ie. if the module is imported, the __name__ variable is set
to the module name.

if __name__ == 'main': makes sure that the code under the if statement
is executed only if current module is executed directly and not when
imported into another module. It is useful for testing modules."""

def line():
    print(f"this sentence is from {__name__} module")


def line_2(name: str):
    """Takes the current module name as an argument in a string format"""

    print(f'this line is called from {name} module')

if __name__ == '__main__':
    line()
    line_2(__name__)
