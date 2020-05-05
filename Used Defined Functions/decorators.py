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

# display = decorator_func(display)     #This is same as line 10~11

@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({0}, {1})'.format(name, age))

#___________decorating with class_____________#
@decorator_class
def display2():
    print("Display2 function ran")

# display2 = decorator_class(display2)     #This is same as line 30~31

@decorator_class
def display_info2(name, age):
    print('display_info2 ran with arguments ({0}, {1})'.format(name, age))


display_info2('Bob', 24)
display2()