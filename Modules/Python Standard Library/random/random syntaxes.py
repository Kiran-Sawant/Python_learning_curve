"""https://docs.python.org/3.7/library/random.html
   Python uses the Mersenne Twister as the core generator.
   It produces 53-bit precision floats and has a period of 2**19937-1.
   The underlying implementation in C is both fast and threadsafe.
   The Mersenne Twister is one of the most extensively tested random number
   generators in existence. However, being completely deterministic,
   it is not suitable for all purposes, and is completely unsuitable
   for cryptographic purposes."""

import random as ran

# seed()
"""The random number generator needs a number to start with (a seed value),
   to be able to generate a random number. By default the random number generator
   uses the current system time"""
# ran.seed(10)

numbers = list(range(1, 101))

# .choise() returnes a random value from the passed iterable.
print(f".choice(): {ran.choice(numbers)}\n")

# .choices(i, k) returns a list of k values randomly selected from the specified iterable.
print(f".choices(): {ran.choices(numbers, k=12)}")    # k defines the length of returned list.

# .randrange() returns a random number from the given range
print(f'.randrange(): {ran.randrange(1, 5000, 3)}\n')

# .randint() does not support a step function
print(f'randint(): {ran.randint(1, 5000)}')

# .shuffle() Takes a sequence and returns the sequence in a random order
ran.shuffle(numbers)
print(f"shuffled numbers: {numbers}")

# .sample() returns a sample from passed population sequence.
j = ran.sample(numbers, k=4)                         # k defines the sample size
print(f"Sample from numbers: {j}")

# .uniform() returns a random float from the passed range.
print(f".uniform(): {ran.uniform(60, 90)}")          # 60 & 90 both are included


#_________________________randoms based on statistical distribution________________________________#
# .betavariate() returns a float between 0 & 1 based on beta distribution
print(ran.betavariate(80, 100))

# .triangular() returns a random float such that low <= f <= high and with the specified mode between those bounds.
print(f"triangular(): {ran.triangular(1, 100, 66)}")     # Here, 66 is the mod

# .expovariate() returns a random float number between 0 & 1, or between 0 & -1 if the parameter is negative,
# based on the Exponential distribution.
ran.expovariate()

# Returns a random float number between 0 & 1 based on the Gamma distribution
ran.gammavariate()

# Returns a random float number between 0 & 1 based on the Gaussian distribution
ran.gauss()

# Returns a random float number between 0 & 1 based on a log-normal distribution
ran.lognormvariate()

# Returns a random float number between 0 & 1 based on the normal distribution
ran.normalvariate()

# Returns a random float number between 0 & 1 based on the von Mises distribution
ran.vonmisesvariate()

# Returns a random float number between 0 & 1 based on the Pareto distribution
ran.paretovariate()

# Returns a random float number between 0 & 1 based on the Weibull distribution
ran.weibullvariate()

#__________________________________Working with states________________________________________#
# Generate a random number
print(ran.random())

# capture the state of random generator machine
state = ran.getstate()

print(ran.random())
# set the state of random generator machine
ran.setstate(state)

# the next random number will be the same as when you captured the state
print(ran.random())