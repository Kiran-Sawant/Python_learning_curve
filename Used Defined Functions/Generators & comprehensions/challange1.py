text = input("Please Enter Your Text: ")

output = list()
for x in text.split():
    output.append(len(x))
print(f"Loop output: {output}")

output2 = [len(x) for x in text.split()]
print(f"Comprehension output: {output2}")

output = []
for x in text.split():
    output.append((x, len(x)))
print(f"Loop output: {output}")

output3 = list((x, len(x)) for x in text.split())
print(f"Comprehension Output: {output3}")