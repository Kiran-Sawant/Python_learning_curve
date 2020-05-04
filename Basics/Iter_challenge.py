list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Chodu"]

iterator = iter(list_1)

for i in range(len(list_1)):
    print(next(iterator))

print("\n")

for items in list_1: #both the for loops do the same thing
    print(items)