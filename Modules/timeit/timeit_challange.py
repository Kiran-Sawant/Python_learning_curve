"""FAiled"""
import timeit

# def deco(func):
#     def inner():
#         return func(10)
#     return inner

# def deco2(func):
#     def inner():
#         return func(10)
#     return inner

test1="""\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

print(fact(10))
"""

test2="""\
def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))
"""

result1 = timeit.timeit(test1, number=1000)
result2 = timeit.timeit(test2, number=1000)
print(result1)
print(result2)