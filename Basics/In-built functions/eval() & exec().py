# Function that returns a quadratic equation
test="""\
def build_equation(a, b, c):                        #Firstclass function
    '''Returns the function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c               #lambda as a closure

k = build_equation(2, 3, -5)
print(k(5))                                         #arguments passed are assigned to lambda(x)

j = build_equation(3, 0, 1)(2)
print(j)\n"""

#___________eval()__________#
"""The eval() function evaluates the specified expression, if the
    expression is a legal Python statement, it will be executed."""

k = eval('print(46456)')

#__________exec()__________#
"""The exec() function accepts large blocks of code, unlike the eval()
    function which only accepts a single expression"""

j = exec(test)
