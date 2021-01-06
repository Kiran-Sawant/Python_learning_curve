"""The logging module can be used to keep a log of activities that you want to track.
    logging requires a logger to keep log. by default it uses the root logger that is needed
to be configured using .basicConfig() before making log calls.
    log calls are needed to be placed at appropriate places with a log message, whenever that
codeblock runs, The log call will trigger a log based on the configuration.

    logging has 5 different levels depending on the nature of activity, they are DEBUG, INFO,
WARNING, ERROR & CRITICAL (In that order).
    By default the level is set to WARNING, ie. the logger will not catch any calls made by a
caller with level below it (DEBUG & INFO). If you set the level to INFO, calls from DEBUG will be
ignored.

PyDoc: https://docs.python.org/3/library/logging.html """

import logging as log

#____________Configuring logging___________#
"""logging.basicConfig() configures root logger settings globally.
level: DEBUG, INFO, WARNING, ERROR, CRITICAL
format: https://docs.python.org/3/library/logging.html#logrecord-attributes"""

file_path = __file__.replace('Logging Basics.py', 'test.log')
log.basicConfig(filename=file_path, level=log.DEBUG,
                format='%(asctime)s:%(levelname)s:%(message)s')        # Setting logging level to DEBUG, globally.
                                                                       # Setting a logging file.

def add(x, y: int):
    return x + y

def subtract(x, y: int):
    return x - y

def multiply(x, y: int):
    return x * y

def divide(x, y: int):
    return x / y

num1 = 10
num2 = 5

# Making log calls
addition = add(num1, num2)
log.debug(f"Addition of {num1} & {num2} is {addition}")         # Printing debug log

subtraction = subtract(num1, num2)
log.info(f"subtraction of {num1} with {num2} is {subtraction}") # Printing info log

product = multiply(num1, num2)
log.error(f"Product of {num1} & {num2} is {product}")           # Printing error log

quotent = divide(num1, num2)
log.warning(f"Division of {num1} by {num2} is {quotent}")       # Printing warning log