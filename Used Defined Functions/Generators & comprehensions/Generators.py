#_______Defining a generator_______#
def square_numbers(nums):
    for i in nums:
        yield (i * i)

#____________Calling a generator____________#
"""A generator must be called through a variable.
    Calling it directly will reset the generator
    everytime its called."""

nums = square_numbers([1, 2, 3, 4, 5])      #Generator object

for i in nums:
    print(i)
