menu = list() #list initialization
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if 'spam' not in meal:
        print(meal)

print('-'*40)

def not_spam(meal: list):
    return 'spam' not in meal

def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals

print(spamless_filter())