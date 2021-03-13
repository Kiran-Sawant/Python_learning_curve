"""Unlike many other languages Python as support for multiple inheritance,
wherein one class can inherit from multiple class at once as on line-22 & 25.
However, one must keep the Method Resolution Order(MRO) in mind. In the example
below both base classes hav a method with same name, both the child classes inherit
the same base classes but who's 'do' method will be executed depends on the order
in which they are passed in the parenthesis.
A rule of thumb is when inheriting multiple classes the most basic/general purpose class
should be rightmost, and the most specilised class must be left most.
If your script has multi-level inheritance structure, then the most grand-parent class
should be rightmost and so on."""

class A():

    def do(self):
        print('A')

class B():

    def do(self):
        print('B')

class AB(A, B):
    pass

class BA(B, A):
    pass

AB().do()           # Prints A
BA().do()           # Prints B
