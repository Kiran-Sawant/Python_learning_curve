"""A decorator function consists of a First-class function that takes
the function on which it is decorated on, as an argument, and returns the
closure function.
    The closure function can take arguments that it will pass to the
decorated function. It performs the defined operation and finally returns
the original decorated function.
    The closure can access variables in its non-local scope even after the
first-class function is done executing.
    Decorator functions are used to perform tasks that might needed to be
performed everytime before a function is called, eg: logging the time & arguments
of a function call, making a database entry everytime a function is called, etc.

    Decorator classes are implimented using a __call__() Magic method. This 
method makes the object callable, ie. whenever the object is called using a
pair of parenthesis (object_name()) the suite inside the __call__() method
will be executed.
    __init__() acts as an outer function and the __call__() function perform
the operation and returns the decorated function."""

#____________Defining a decorator Function____________#
def decorator_func(original_func):

    def wrapper_func(*args, **kwargs):      #*args & **kwargs help take functions with multiple arguments as argument
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper_func

#____________Defining a decorator Class____________#
class decorator_class():
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("call method executed this before {0}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)

#______________Using decorators______________#
@decorator_func
def display():
    print("Display function ran")

# display = decorator_func(display)     #This is same as line 39~40

@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({0}, {1})'.format(name, age))

#___________decorating with class_____________#
@decorator_class
def display2():
    print("Display2 function ran")

# display2 = decorator_class(display2)     #This is same as line 50~51

@decorator_class
def display_info2(name, age):
    print('display_info2 ran with arguments ({0}, {1})'.format(name, age))


display_info2('Ken', 21)