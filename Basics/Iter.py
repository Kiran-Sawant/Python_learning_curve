string = "1234567890"
iterator = iter(string) #iter() explicitly calls one object @ a time from iterable string
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for char in string: #a for loop implicitly uses iter
    print(char)