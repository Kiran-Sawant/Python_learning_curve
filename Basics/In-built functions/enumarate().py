"""enumerate() method adds a counter (starting from 0) to an iterable and returns it in
    a form of enumerate object. This enumerate object can then be used directly in for
    loops or be converted into a list of tuples, dictionaries or a tuple of tuples.
    enumarate() is like adding a serial no to the outputs of an iterator."""

x = ['apple', 'banana', 'cherry', 'killer', 'Bean', 'himmaniler']
j = enumerate(x)                #creating an enumarate object
for i in j:
    print(i)

print(list(enumerate(x, start=1)))       #creating an enumarated list with count starting from 1

for srno, title in enumerate(x):
    print(srno)

print(dict(enumerate(x)))       #creating a dict from enumarate, where
                                #Sr.no is the key