menu = list() #list initialization
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
menu.append(["chicken", "chips"])

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(f"Meals in loop: {meals}\n")

#___________Using conditional comprehensions___________#
meals2 = list(meal for meal in menu if "spam" not in meal and "chicken" not in meal)
print(f"Meals2: {meals2}\n")

fussy_meal = list(meal for meal in menu if ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal))
print(f"Fussy meal: {fussy_meal}")