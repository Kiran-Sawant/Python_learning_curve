def square(x):
    return x * x

'''Not giving parenthesis after a function name
    assigns the function to the variable and then
    the variable can be used to call the function'''
f = square
# print(f(9))


def cube(x):
    return x*x*x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

choice = input("for square press 's' & for cube press 'c'")
if choice == 's':
    num = my_map(f, [1,2,3,4,5])
    print(num)
elif choice == 'c':
    num = my_map(cube, [1,2,3,4,5])
    print(num)
else: 
    print('Wrong choice')
