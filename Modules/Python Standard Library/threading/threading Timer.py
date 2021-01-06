"""This class represents an action that should be run only
after a certain amount of time has passed — a timer."""

from threading import Timer

def Hello(name):
    print(f'Hello {name}')

t = Timer(5, Hello, ('Kiran',))
t.start()