menu = [["egg", "spam", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ['Cheeze', 'Jam', 'Tost']]

for meal in menu:
    if 'spam' not in meal:
        print(meal)

print('-'*40)

"""filter(f, i) takes a function name & an iterable as arguments.
returns the iterable values for which the function returns True."""

# returns False if spam in meal
def not_spam(meal: list):
    return 'spam' not in meal

def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals

print(spamless_filter())