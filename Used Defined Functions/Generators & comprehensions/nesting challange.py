for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

for exp in [[(x, x*y) for y in range(1, 11)] for x in range(1, 11)]:
    for j in exp:
        print(j)

# Generator expression implimentation
for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)

