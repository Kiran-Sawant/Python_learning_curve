"""This script creates 2 threads that work on 2 different functions each.
threading completes the program in 2 sec, which could've taken 4 if done
linearly. we want Queue to use its .join() method, in absence of which the
program would move ahead and terminate even if the functions are not completed."""

import threading as thrd
import time
from queue import Queue

def func_1():
    q.get()
    time.sleep(2)
    print('Hello There')
    q.task_done()

def func_2():
    q.get()
    time.sleep(2)
    print('Hello World')
    q.task_done()

q = Queue()
q.put(1)
q.put(2)

# Creating 2 threads
t1 = thrd.Thread(target=func_1)
t2 = thrd.Thread(target=func_2)

# Making them daemonic
# t1.daemon=True
# t2.daemon=True

time_1 = time.time()            # Recording start time

# Starting the threads
t1.start()
t2.start()

# Blocking Program
q.join()
# func_1()
# func_2()

print(f"Time taken: {time.time() - time_1}")