'''adding more layers to the first-class function makes the code more complex'''

def prefix(pre):        #defining a decorator function that takes an argument and returns a closure
    def decorator_func(original_func):
        def wrapper(*args, **kwargs):
            print(pre, "Executed before ", original_func.__name__)
            result = original_func(*args, **kwargs)
            print(pre, "Executed after ", original_func.__name__)
            return result
        return wrapper
    return decorator_func

@prefix('LOG: ')
def display_info(name, age):
    print("display_info ran with ({0}, {1})".format(name, age))

display_info('Bob', 42)