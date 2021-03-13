"Taken From: https://pybay.com/site_media/slides/raymond2017-keynote/threading.html"
import threading
import queue
import time
import random

counter = 0

"""
#_________A Simple Job____________#
print('Starting up')
for i in range(10):
    counter += 1
    print(f'The count is {counter}')
    print('---------------')
print('Finishing up')
"""
"""
#_________Function Style_________#

def worker():
    'My job is to increment the counter and print the current count.'
    global counter

    counter += 1
    print(f'The count is {counter}')
    print('---------------')

print('Starting up')
for i in range(10):
    worker()
print('Finishing up')
"""
"""
#___________Using Simple threading___________#
def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')

print('Starting up')
for i in range(10):
    threading.Thread(target=worker).start()
print('Finishing up')
"""
#________Fuzzing________#
##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible
# Set FUZZ = False to disable fuzzing
FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.randrange(1, 3))

###########################################################################################
"""
#________Simple Threading with Fuzzing___________#
# in this method the counter never reaches 10

def worker():
    'My job is to increment the counter and print the current count'
    global counter

    fuzz()
    oldcnt = counter
    fuzz()
    counter = oldcnt + 1
    fuzz()
    print(f'The count is {counter}', end='')
    fuzz()
    print()
    fuzz()
    print('---------------', end='')
    fuzz()
    print()
    fuzz()

print('Starting up')
fuzz()
for i in range(10):
    threading.Thread(target=worker).start()
    fuzz()
print('Finishing up')
fuzz()
"""

#______________Threading the right Way________________#
counter_queue = queue.Queue()

def counter_manager():
    'I have EXCLUSIVE rights to update the counter variable'
    global counter

    while True:
        increment = counter_queue.get()
        counter += increment
        print_queue.put([
            f'The count is {counter}',
            '---------------'])
        counter_queue.task_done()

t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
# del t

###########################################################################################

print_queue = queue.Queue()

def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'
    while True:
        job = print_queue.get()
        for line in job:
            print(line)
        print_queue.task_done()

t2 = threading.Thread(target=print_manager)
t2.daemon = True
t2.start()
# del t

###########################################################################################

def worker():
    'My job is to increment the counter and print the current count'
    counter_queue.put(1)

print_queue.put(['Starting up'])
worker_threads = []
for i in range(10):
    t = threading.Thread(target=worker)     # Creating 10 non-daemonic threads
    worker_threads.append(t)
    t.start()
for t in worker_threads:
    t.join()                                # joining non-daemonic threads

counter_queue.join()
print_queue.put(['Finishing up'])
print_queue.join()