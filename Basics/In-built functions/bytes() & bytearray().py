"""byte() returns an immutable wherelse
    bytearray returns a mutable object"""

#____byte_____#
x = bytes(5)
print(f"bytes() of an int: {x}")

k = bytes('Kiran'.encode('UTF-8'))
print(f"bytes() of a string: {k}\n")

#____bytearray____#
y = bytearray(3)
print(f"bytearray() of an int: {y}")

j = bytearray('Killer Bean'.encode('ASCII'))
print(f"bytearray() of a string: {j}")