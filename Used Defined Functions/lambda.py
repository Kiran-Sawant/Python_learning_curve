"""Lambda functions have no name.
    they must be expressed in one line.
    Keyword lambda is followed by a number of parameters,
    Then a colon and then the expression.
    The output of expression is returned automatically"""

# A program to return 3x + 1
f = lambda x: 3*x +1

print(f(2))

# Combine first & last name into full name
full_name = lambda fn, ln: fn.strip().title() +' '+ ln.strip().title()

print(full_name('KIRAN', 'SaWaNt  '))

#__________actual use of a lambda___________#
#Sorting a list by last name
names = ["H. G. Wells", "Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert"]

names.sort(key=lambda name: name.split(' ')[-1].lower())
print(names)

# Function that returns a quadratic equation
def build_equation(a, b, c):                        #Firstclass function
    '''Returns the function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c               #lambda as a closure

k = build_equation(2, 3, -5)
print(k(5))                                         #arguments passed are assigned to lambda(x)

j = build_equation(3, 0, 1)(2)
print(j)