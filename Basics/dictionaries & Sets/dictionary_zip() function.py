name = str(input("Enter your name: "))
job = str(input("Enter you job: "))
age = int(input("Enter you age: "))
list1 = [name, job, age]
list2 = ["name", "job", "age"]
collection = dict(zip(list2, list1))
print(collection)
