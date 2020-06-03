import collections as col

#____________________named tuples_______________________#
# Creating a named tuple object_________#
tup = col.namedtuple('Color', ['x', 'y'])

# Creating a named tuple
k = tup('red', 'green')

# Accessing values
print(k.x)          # accessing through names
print(k[1])         # accessing through index

m, l = k            # unpacking like a normal tuple

# ._make() method_______________________#
""" It creates a named tuple object from an
    existing iterable like a list or tuple"""

colour = ['purple', 'white']        # existing itearble

j = tup._make(colour)               # creating named tuple from an iterable

# ._asdict() method_____________________#
""" It returns an OrderedDict that maps the
    names to their values"""

jdict = j._asdict()                 # converting to an OrderedDict object
print(jdict)

# ._replace() method_____________________#
""" It replaces the current values with the
    passed values"""

j._replace(x='Grey')
print(j)

# ._fields________________________________#
""" returns the names of a passed named tuple"""

print(j._fields)

# .field_defaults_________________________#
""" returns the default values of the names if
    set while creating the named tuple"""

print(j._field_defaults)


#_______________________deque Objects__________________________#
""" Deques are a generalization of stacks and queues
    (the name is short for “double-ended queue”).
    Deques support thread-safe, memory efficient appends
    and pops from either side of the deque with approximately
    the same O(1) performance in either direction."""

# Creating a deque Object
deck = col.deque(range(50))

# .append() method_______________#
""" Adds values to the right side of the deque."""

deck.append('Right Insersion')

# .appendleft() method_______________#
""" Adds values to the left side of the deque."""

deck.appendleft('Left Insersion')

# .extend() method__________________#
""" Extend the right side of the deque by
    appending elements from the iterable argument."""

deck.extend(range(50, 56))

# .extendleft() method_______________#
""" Extend the left side of the deque by appending
    elements from the iterable argument. Note,
    the series of left appends results in reversing
    the order of elements in the iterable argument."""

deck.extendleft(range(0, -6, -1))

# .index() method_____________________#
""" returns the index value of first match of passed value"""

print(deck.index(-5))

# .insert() method_____________________#
""" Inserts the passed value into the passed position(not index)"""

deck.insert(1, -6)

# .pop() method_________________________#
""" Remove and return an element from the right side of the deque"""

deck.pop()

# .popleft() method_____________________#
""" Remove and return an element from the left side of the deque."""

deck.popleft()

# .remove() method______________________#
"""Remove the first occurrence of value."""

deck.remove(0)

# .reverse() method_____________________#
""" Reverse the elements of the deque in-place"""

deck.reverse()

# .count() method_______________________#
""" returns the number of occurence of the passed value"""

print(deck.count(30))

# .rotate() method______________________#
""" will shift right all the values in the deque times the value
    passed, leftappending the values in the end. pass negative
    values to rotate towards left."""

deck.rotate(2)

print(deck)

#___________________Counter Objects_____________________#
""" Gives a tally of all the elements in an iterable"""

cnt = col.Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue', 'orange']:
    cnt[word] += 1

# .most_common() method_________________#
""" Return a list of the n most common elements and their
    counts from the most common to the least."""

print(cnt.most_common(2))           # gives 2 most commonly occuring values in the list.
