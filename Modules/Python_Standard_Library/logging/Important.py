"""The Problem with using root logger is that if a module
that you have imported uses root logger and the main module
uses root logger as well, then the root logger will be configured
in the imported module as the imported module is executed at import,
and will not be reconfigured in the main module, therefore it will
become impossible to maintain 2 separate log files for two different modules.

If we run this script it will log calls in the main module in employee.log
file insted of test.log, as filename was set while importing employee
and it ignores basicConfig @ line 16."""

import logging as log
import employee

file_path = r"D:\my_space\software_projects\Python\Learning_curve\Modules\Python Standard Library\logging"
log.basicConfig(filename=file_path + r'\test.log', level=log.DEBUG,
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

addition = add(num1, num2)
log.debug(f"Addition of {num1} & {num2} is {addition}")         # Printing debug log

subtraction = subtract(num1, num2)
log.info(f"subtraction of {num1} with {num2} is {subtraction}") # Printing info log

product = multiply(num1, num2)
log.error(f"Product of {num1} & {num2} is {product}")           # Printing error log

quotent = divide(num1, num2)
log.warning(f"Division of {num1} by {num2} is {quotent}")       # Printing warning log