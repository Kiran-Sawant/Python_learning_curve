'''This script keeps a log of how many times a function
   was executed & what arguments were passed to it'''

import logging as log
import time
import functools as ft      #additional tools for defining functions

#____________________Defining Decorator function______________________#
def my_logger(func):
    log.basicConfig(filename='{0}'.format(func.__name__), level=log.INFO)       #configuring log file

    @ft.wraps(func)
    def wrapper(*args, **kwargs):   # Here wrapper has access to args & kwargs of func
        log.info("Ran with args: {0}, and kwargs: {1}".format(args, kwargs))
        return func(*args, **kwargs)

    return wrapper


def my_timer(func):

    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        delta = time.time() - t1
        print("{} ran in : {} sec".format(func.__name__, delta))
        return result

    return wrapper

#_________________Using decorators on functions___________________#
'''Here, the my_logger function runs before the display_info function'''
@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({0}, {1})'.format(name, age))

'''Here, the my_timer function runs before the display function'''
@my_timer
def display():
    print("Display function ran")

#_______________________applying multiple decorators_________________________#
'''while applying multiple decorators to a function it is necessary to apply
   the @functools.wraps() decorater of functools module to the closures of the decorator
   functions or else the second decorator takes the wrapper function of the
   first decorator as an argument & not the function on which the decorator is applied to'''

@my_logger
@my_timer
def display2():
    print("Display2 function ran")


display_info('Optimus Prime', 104)
display()
display2()

print(display_info.__name__)