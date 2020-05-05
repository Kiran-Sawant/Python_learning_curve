'''Closures are the enclosed functions inside of a function.
   Closures can access variables defined in their outer scope
   even when the outer function is finished executing'''

def outer_func(msg):
    message = str(msg)

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()