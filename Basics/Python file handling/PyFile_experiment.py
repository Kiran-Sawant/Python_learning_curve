name = ""
print("you can press 'q' to exit")

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    age = int(input("Enter your age {0}: ".format(name)))
    data = [name, age]
    with open('database.txt', mode='a') as newData:
        print(data[0] + ': ', data[1], file=newData)