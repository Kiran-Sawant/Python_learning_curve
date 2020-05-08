"""The compile() function returns the specified source as a code object,
    ready to be executed.
    Param1: The source to compile, can be a String, a Bytes object, or an AST object
    Param2: The name of the file that the source comes from. If the source does not
    come from a file, you can write whatever you like"""

#____________Code to compile_____________#
test1 = """\
def build_equation(a, b, c):                        #Firstclass function
    '''Returns the function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c               #lambda as a closure

k = build_equation(2, 3, -5)
print(k(5))                                         #arguments passed are assigned to lambda(x)

j = build_equation(3, 0, 1)(2)
print(j)\n"""

#_______compiling_______#
x = compile(test1, 'test', 'exec')      #For single-line code use 'eval' & for multiline use 'exec'
exec(x)

print(f"Type of x: {type(x)}")