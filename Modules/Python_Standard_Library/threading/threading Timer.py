"""This class represents an action that should run only
after a certain amount of time has passed — a timer.
Every Timer instance runs on its own thread."""

from threading import Timer

def Hello(name):
    print(f'Hello {name}')

# Timer Object with an interval of 5 sec
t = Timer(5, Hello, ('Kiran',))
t.start()