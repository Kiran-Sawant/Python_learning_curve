import itertools as it
import operator

# .count() method returns a counter
counter = it.count(start=1, step=1)

# Using the .count() method
data = list(range(100, 500, 100))

daily_data = list(zip(it.count(start=-1, step=-1), data))

for i in daily_data:
    print(i)

# .cycle() method____________________________________________#
""".cycle() method does not stop after the completion of the
    iterable it keeps repeating the values of the iterable"""

counter = it.cycle([1, 2, 3])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# .repeat method___________________________________________#
""" .repeat() returns the object for a specified ammount of
    time, if not specified returns the object indefinetly"""

counter = it.repeat(2, times=2)

#______________Combinations & Permutations_________________#

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]
names = ['Corey', 'Nicole']

result = it.combinations(letters, 2)

for item in result:
    print(item)

result2 = it.permutations(letters, 2)

for item in result2:
    print(item)

# .product() method___________________________#
""" .product() returns the cartician product,
    ie. possible permutations where values can
    repeat specified times"""

result3 = it.product(numbers, repeat=2)

for item in result3:
    print(item)

# .combinations_with_replacement()_________#
"""Same as .product() but returnes possible
    combinations insted of permutations"""

result4 = it.combinations_with_replacement(numbers, 2)

for item in result4:
    print(item)

# .chain() method______________________________________#
""" .chain() combines the output of passed iterables in
    the order they are passed, regardless of the type of
    iterable passed."""

combined = it.chain(letters, numbers, names)

for item in combined:
    print(item)

# .islice() method_________________________________#
""" .islice() grabes a slice of passed iterable."""

result = it.islice(range(10), 2, 8)         # grabbing values from index 2~8

# .compress() method_________________________________#
""" .compress() returns the values in passed iterable
    that are true in the corrosponding selector iterable.
    The selector iterable can be a generator as well."""

selectors = [True, True, False, True]

result = it.compress(letters, selectors)

# .filterfalse() method__________________________#
""" .filterfalse() is the opposite of compress"""

result2 = it.filterfalse(letters, selectors)

# .dropwhile() method_________________________#
""" .dropwhile() is the same as .filterfalse,
    however it stops applying the filter after
    it encounters a value that satisfyes the criteria."""

result3 = it.dropwhile(letters, selectors)

# .takewhile() method_____________________________#
""" .takewhile() is the opposite of .dropwhile()"""

result3 = it.takewhile(letters, selectors)

# .accumulate() method_______________________________________#
""" returns a cumulative result. cummulative sum by default"""

result4 = it.accumulate(numbers)                # calculating cummulative sum
for i in result4:
    print(i)

result5 = it.accumulate(numbers, operator.mul)  # calculating cummulative product
for i in result5:
    print(i)
