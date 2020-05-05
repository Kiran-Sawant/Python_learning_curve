def printBackwards(*args, end=' ', **kwargs):
    for arg in args[::-1]:
        print(arg, end=end, **kwargs)


printBackwards('kill', 'me', 'First', 'Second', end=' ')