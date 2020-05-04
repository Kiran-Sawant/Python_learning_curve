string = set(input("Type a small sentence:  "))
print(string)
#vowels = {"a", "e", "i", "o", "u", " ", "A", "E", "I", "O", "U"}
vowels = frozenset("aeiou AEIOU")
string.difference_update(vowels)
print(sorted(string))