"""all() checks if all the values in an iterable is True
    if not passes False. any() checks if there is atleast
    one True value in given iterable if not passes False."""

entries = [1,2,3,4,5]

print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

entry = []

print(f"all: {all(entry)}")     # all() returns True for an empty iterable
print(f"any: {any(entry)}")