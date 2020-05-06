burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']

# Comprehension with two iterating parts
meals = list((burger, topping) for burger in burgers for topping in toppings)   # here expression is a tuple with 2 iterating parts burger & topping.
for i in meals:
    print(i)

print('+'*20)

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

"""Nested comprehension is where the expression is itself
   a comprehension which is then iterated over an iterator"""
# Using nested comprehension
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)