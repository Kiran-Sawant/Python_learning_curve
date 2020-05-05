"""https://docs.python.org/3/library/exceptions.html"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
try:
    print(factorial(80))
except (RecursionError):
    print("This program cannot calculate factorials that large")

#______Using multiple exceptions______#
"""always put the most specific exception at the top"""

try:
    print(factorial(9000))
except (RecursionError, OverflowError):         #passing multiple exceptions
    print("This program cannot calculate factorials that large")
except ZeroDivisionError:                       #Another way of passing multiple exceptions
    print("What are you doing! dividing by zero")
print("Program terminated")