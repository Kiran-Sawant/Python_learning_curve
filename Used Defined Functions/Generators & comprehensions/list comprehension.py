print(__file__)

"""list comprihensions are like set builder method
    of representing sets in mathematical sets.
    It consists of a mathematical expression and an iterator."""

my_nums = [x*x for x in [1,2,3,4,5]]        #here, my_nums is a list object

print(my_nums)

for num in my_nums:
    print(num)