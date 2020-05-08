"""The hash() method returns the hash value of an object if it has one.
    Hash values are just integers which are used to compare dictionary
    keys during a dictionary lookup quickly.
    hash values of objects with equal values are same."""

x = 'Killer'
y = 'Killer'
z = 'Bean'

print(f"hash('Killer'): {hash(x)}")
print(f"hash('Killer'): {hash(y)}")
print(f"hash('Bean'): {hash(z)}")