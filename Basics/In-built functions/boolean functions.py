#___________bool()____________#
"""The bool() function returns the boolean value of a specified object.
The object will always return True, unless:
The object is empty, like [], (), {}
The object is False
The object is 0
The object is None"""
print(f"bool(False): {bool(False)}\nbool([]): {bool([])}\n"
       f"bool(26): {bool(26)}\n")

#___________any() and all()______________#
"""all() checks if all the values in an iterable is True
    if not passes False. any() checks if there is atleast
    one True value in given iterable if not passes False."""

entries = [1,2,3,4,5]

print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

entry = []

print(f"all: {all(entry)}")     # all() returns True for an empty iterable
print(f"any: {any(entry)}\n")

#________callable()_________#
"""The callable() function returns True if the specified
    object is callable, otherwise it returns False."""

def x():
    a = 5
    return a

print(f"Callability of x: {callable(x)}")