"""The slice() function returns a slice object.
    A slice object is used to specify how to slice a sequence.
    You can specify where to start the slicing, and where to end.
    You can also specify the step, which allows you to slice only
    every other item.

    Syntax: slice(start, end, step)"""

a = ("a", "b", "c", "d", "e", "f", "g", "h")
b = "Killer Bean Forever"
c = list(pow(x, 3) for x in range(1, 15))

# Creating a slice object starting from 1 upto 5.
x = slice(1, 6)

print(a[x])
print(b[x])
print(c[x])