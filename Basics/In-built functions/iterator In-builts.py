#________iter() & next()________#
string = "1234567890"
iterator = iter(string) #iter() explicitly calls one object @ a time from iterable string
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for char in string: #a for loop implicitly uses iter
    print(char)

#______max()_______#
"""Returns the maximum value in an iterable."""

print(f"Max of string: {max(string)}")

#______min()_______#
"""Returns the minimum value in an iterable."""

print(f"Min of string: {min(string)}")

#______reversed()______#
"""Returns the passed iterable in reversed order."""

lst = ['Albert', 'Richard', 'Maxwell', 'Andre']

k = reversed(lst)
for i in k:
    print(i)