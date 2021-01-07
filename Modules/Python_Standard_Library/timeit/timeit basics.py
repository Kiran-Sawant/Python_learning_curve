import timeit

setup = """\
gc.enable()
locations = {0:"You are sitting in front of the computer",
             1:"You are standing in front of the road before a brick building",
             2:"You are at the top of a hill",
             3:"You are inside a buiding",
             4:"You are in a valler besides a stream",
             5:"You are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "E":3, "N":5, "S":4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"W":1, "Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2, "S":1,"Q":0}}
"""

locations = {0:"You are sitting in front of the computer",
             1:"You are standing in front of the road before a brick building",
             2:"You are at the top of a hill",
             3:"You are inside a buiding",
             4:"You are in a valler besides a stream",
             5:"You are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "E":3, "N":5, "S":4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"W":1, "Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2, "S":1,"Q":0}}

def nested_loop():
    result = list()
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
        return result

def looped_comprehension():
    result = list()
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
        return result

def nested_comprehensions():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
    return exits_to_destination_3

print(nested_loop())
print(looped_comprehension())
print(nested_comprehensions())
# Using timeit() method
result_1 = timeit.timeit(nested_loop, setup, number=1000)
result_2 = timeit.timeit(looped_comprehension, setup, number=1000)
result_3 = timeit.timeit(nested_comprehensions, setup, number=1000)
print(f"\nNested loop timing: {result_1}")
print(f"Looped Comprehension timing: {result_2}")
print(f"Nested Comprehension timing: {result_3}")