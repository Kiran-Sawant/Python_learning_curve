#_________complex()__________#
"""The complex() function returns a complex number by
    specifying a real number and an imaginary number.
    Syntax:- complex(real, imaginary)"""
x = complex(3, 5)
print(f"complex of 3, 5: {x}")

y = complex('3+5j')     #passing a string as an argument, string must be passed without spaces
print(f"complex '3+5j': {y}\n")

#_________divmod()___________#
"""The divmod() function returns a tuple containing the
    quotient  and the remainder when argument1 (divident)
    is divided by argument2 (divisor).
    Syntax: divmod(divident, divisor)"""

xa = divmod(5, 2)       #dividing 5 by 2
print(f"divmod(5, 2): {xa}\n")

#________int() & round()_________#
"""int() returns truncated float
    round() takes 2 args. the number and the precision level"""

ya = int(3.9999)
print(f"int(3.999): {ya}")

yb = round(3.9699456789, 2)     #passing number and precision level
print(f"round(3.9699): {yb}\n")

#________pow()__________#
"""pow() returns the answer of 1st arg to the power of 2nd arg
    If a 3rd arg is passed returns the modulo of answer by 3rd arg.
    Syntax: pow(x, y, z) = (x ** y) % z"""

xc = 4 ** 3
print(xc)

xb = pow(4, 3)
print(xb)

#________sum()_________#
"""The sum() function returns the sum of all items in an iterable."""

def test():
    for i in range(1, 200, 2):
        yield i
    
k = test()
m = sum(k)      #returning sum of all numbers in range 1-200 with count 2
print(m, '\n')

#________format()_________#
"""The format() function formats a specified value into a specified format.
    Syntax: format(value, format)
    resource link: https://www.w3schools.com/python/ref_func_format.asp"""

print(format(0.5, '%'))
print(format(55, 'X'))
