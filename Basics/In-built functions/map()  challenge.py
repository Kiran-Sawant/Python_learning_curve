import timeit

text = "What have the romans ever done for us?"

def comp():
    capitals = [char.upper() for char in text]
    return capitals

# capitals using maps
def maping():
    map_capitals = list(map(str.upper, text))
    return map_capitals

def word_comp():
    words = list(word.upper for word in text.split(' '))
    return words

# Words using map
def word_map():
    map_words = [map(str.upper, text.split(' '))]
    return map_words


print(timeit.timeit(comp, number=10000, globals=globals()))
print(timeit.timeit(maping, number=10000, globals=globals()))
print(timeit.timeit(word_comp, number=10000, globals=globals()))
print(timeit.timeit(word_map, number=10000, globals=globals()))