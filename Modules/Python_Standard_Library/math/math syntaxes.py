import math

#____________math constants______________#

print(f"Euler's number: {math.e}")
print(f"Positive Infinity: {math.inf}")
print(f"Not a Number Value (NaN): {math.nan}")
print(f"Pi: {math.pi}")
print(f"tau: {math.tau}\n")

#_________Arithmetics__________#

print(f"pow(5, 10) = {math.pow(5, 10)}\n")
# math.ceil
print(f"ceil(5.3): {math.ceil(5.3)}")               # rounds the decimals upwards
print(f"ceil(-5.3): {math.ceil(-5.3)}")             # its the opposite of math.floor
print(f"ceil(22.6): {math.ceil(22.6)}\n")
# math.floor
print(f"floor(5.3): {math.floor(5.3)}")             # rounds the decimals downwards
print(f"floor(-5.3): {math.floor(-5.3)}")           # its the opposite of math.ceil
print(f"floor(22.6): {math.floor(22.6)}\n")

# math.fmod(x, y) returnes remainder of x/y as float
print(f"fmod(67, 7): {math.fmod(67, 7)}")         # almost same as 67 % 7

# math.fabs(x) returns absolute as a float
print(f"fabs(-55.698): {math.fabs(-55.698)}\n")   # same as abs()

# math.factorial(x)
print(f"factorial(12): {math.factorial(12)}\n")

# math.fsum(iterable) returns summation of all values in the iterable
print(f"fsum(range(0, 200, 2)): {math.fsum(range(0, 200, 2))}\n")

# amth.gcd(x, y) returns Greatest common divisor between x & y
print(f"gcd(12, 6): {math.gcd(12, 6)}")

# math.remainder(x, y) returns a value k that makes x completely divisible by y
print(f"remainder(67, 7): {math.remainder(67, 7)}\n")

#______________Permutations & Combinations_______________#       Requires Python 3.8

# math.perm(n, k) returns the number of ways to choose k items from n items with order and without repetition.
# print(f"{math.perm(len(range(1,101)), 20)}")

# math.comb(n, k) returns the number of ways to pick k unordered items from n items, with repetition, known as combinations.
# print(f"{math.comb(len(range(1,101)), 20)}")

#______________Logarithmic Operations__________________#

print(f"log(20, 10): {math.log(20, 10)}")               # log of 20 to the base 10
print(f"log10(150): {math.log10(150)}")                 # log of 150 to the base 10
print(f"log2(160): {math.log2(160)}")                   # log of 160 to the base 2

print(f"gamma(30): {math.gamma(30)}")
print(f"lgamma(30): {math.lgamma(30)}\n")

#__________________Euclidian Geometry___________________#

# math.degrees(rad) converts passed radians into degrees
print(f"degrees(3.14): {math.degrees(3.141592653589793)}")

# math.radians(deg) converts degrees into radians
print(f"radians(180): {math.radians(180)}")

# math.dist(p, q) returns Euclidean distance between two single-dimensional points
# print(f"dist(3, 4): {math.dist(3, 4)}")

# math.hypot(p, b) Find the hypotenuse of a right-angled triangle with perpendicular(p) and base(b)
print(f"hypot(10, 5): {math.hypot(10, 5)}\n")

#_____________Trigonometric Operations_________________#

# math.cos(x) returns the cosine value of x
print(f"cos(30): {math.cos(30)}")
# math.cosh(x) returns the hyperbolic cosine of x
print(f"cosh(30): {math.cosh(30)}")
# math.acos(x) returns arc cosine value of x
print(f"acos(0.5): {math.acos(0.5)}")                   # The values must lie between -1 to 1
# math.acosh(x) returns hyperbolic arc cosine value of x
print(f"acosh(30): {math.acosh(30)}")                   # The values must be greater than 1

# math.sin(x) returns the sin value of x
print(f"sin(30): {math.sin(30)}")
# math.sinh(x) returns the hyperbolic sin of x
print(f"sinh(30): {math.sinh(30)}")
# math.asin(x) returns arc sin value of x
print(f"asin(-1): {math.asin(-1)}")                     # The values must lie between -1 to 1
# math.asinh(x) returns hyperbolic arc sin value of x
print(f"asinh(30): {math.asinh(30)}")                   # The values must be greater than 1

# math.tan(x) returns the tangent value of x
print(f"tan(30): {math.tan(30)}")
# math.tanh(x) returns the hyperbolic tangent of x
print(f"tanh(30): {math.tanh(30)}")
# math.atan(x) returns arc tangent value of x
print(f"atan(0.5): {math.atan(0.5)}")                   # The values must lie between -1 to 1
# math.atanh(x) returns hyperbolic tangent value of x
print(f"atanh(30): {math.atanh(0.5)}\n")                # The values must be between -0.99 & 0.99