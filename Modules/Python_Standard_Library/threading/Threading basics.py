import threading as thrd
import time
from queue import Queue

def func_1():

    time.sleep(2)
    # Returns current Thread.
    print(f"func_1 thread: {thrd.current_thread()}")
    # Returns id of the current Thread.
    print(f"func_1 thread ID: {thrd.get_ident()}")
    print('Hello There')


def func_2():

    time.sleep(2)
    print(f"func_2 thread: {thrd.current_thread()}")
    print(f"func_2 thread ID: {thrd.get_ident()}")
    print('Hello World\n')

# Creating 2 threads.
t1 = thrd.Thread(target=func_1)
t2 = thrd.Thread(target=func_2)

# Making them daemonic.
# t1.daemon=True
# t2.daemon=True

time_1 = time.time()            # Recording start time

# Starting the threads.
t1.start()
t2.start()

# Returns name of the thread Thread-n by default.
print(f"Thread 1 name: {t1.name}")
# Returns True if alive.
print(f"Thread 1 alive?: {t1.is_alive()}\n")

# Gives a number of active threads.
print(f"Active Count: {thrd.active_count()}")
# Give a list of all active threads including dummy-threads.
print(f"enumarate: {thrd.enumerate()}")
# Returns the main thread.
print(f"Main thread: {thrd.main_thread()}")

# Blocking the Program
"""Thread.join() method stops the program from going further
until the joined threads have finished their tasks."""

t1.join()
t2.join()

#__________Executing functions linearly_____________#
# func_1()
# func_2()

print(f"Time taken: {time.time() - time_1}")