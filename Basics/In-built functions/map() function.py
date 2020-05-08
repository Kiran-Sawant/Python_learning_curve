"""A map function takes a function and an iterable, and calls the function
    for each value in the iterable and then stores the values inside of an
    iterable like a list. Remember to give a function name & not to call the
    function itself."""

text = "What have the romans ever done for us?"

capitals = [char.upper() for char in text]
print(capitals)

# capitals using maps
map_capitals = list(map(str.upper, text))
print(map_capitals)

words = list(word.upper for word in text.split(' '))
print(words)

# Words using map
map_words = [map(str.upper, text.split(' '))]
print(map_words)
