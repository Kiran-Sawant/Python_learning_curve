"""This script corrects the problem in the important.py script.
Here, the imported module(custom_loggers) has a custom logger,
and the main script uses custom logger as well, hence they can
keep log on different log files."""

import logging as log
import custom_loggers as cl

#______Creating custom logger for this module_________#
# Creating logger
logger = log.getLogger(__name__)        #__name__ will be printed in the log file#
# setting logger level
logger.setLevel(log.DEBUG)
# Creating a Formatter object
formatter = log.Formatter('%(levelname)s: %(name)s: %(message)s')

#________Creating Handler objects__________#
file_path = __file__.replace('Multilog.py', 'test.log')

# Creating FileHandler, A handler that writes formatted logging records to log files.
file_handler = log.FileHandler(file_path)
file_handler.setLevel(log.DEBUG)      # setting level for FileHandler.
file_handler.setFormatter(formatter)

# Creating  StreamHandler, A handler that writes logging records on console.
stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

# Assigning handler objects to our custom logger.
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x, y: int):
    return x + y

def subtract(x, y: int):
    return x - y

def multiply(x, y: int):
    return x * y

def divide(x, y: int):
    """Logging error tracebacks
    logger.error() will log an error
    logger.exception() will log error & traceback."""
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error(msg="Tried dividing with zero!")
        logger.exception(msg="Tried dividing with zero!")
    else:
        return result

num1 = 10
num2 = 0

addition = add(num1, num2)
"""After you create a custom logger do not forget to use the identifier
of that logger insted of the module name"""
logger.debug(f"Addition of {num1} & {num2} is {addition}")         # Printing debug log

subtraction = subtract(num1, num2)
logger.info(f"subtraction of {num1} with {num2} is {subtraction}") # Printing info log

product = multiply(num1, num2)
logger.error(f"Product of {num1} & {num2} is {product}")           # Printing error log

quotent = divide(num1, num2)
logger.debug(f"Division of {num1} by {num2} is {quotent}")         # Printing warning log