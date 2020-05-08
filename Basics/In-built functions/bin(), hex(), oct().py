"""bin(), hex() & oct() only take an integer object
    as an input and nothing else"""

x = bin(69)
print(f"69 In binary: {x}")

y = hex(69)
print(f"69 In hexadecimal: {y}")

z = oct(69)
print(f"69 In Octal: {z}")