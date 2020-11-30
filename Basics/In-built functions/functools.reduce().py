#______ft.reduce(f, i)______#
"""reduce() applies 2 values of the passed iterable consecutively.
It will take first 2 values from the left and pass it to the function,
then it will take the returned value and the next consecutive value in
the iterable and pass it again to the function and will keep doing it
repetedly till its left with only one value.
Requires a function that takes 2 arguments."""

import functools as ft
import timeit

def calc_values(x, y: int):
    return x * y

numbers = [2, 3, 5, 8, 13]

reduced_value = ft.reduce(calc_values, numbers)
print(reduced_value)

# Without ft.reduce()
result = 1
for x  in numbers:
    result *= x
print(result)

result = calc_values(2, 3)
result = calc_values(result, 5)
result = calc_values(result, 8)
result = calc_values(result, 13)
print(result)
