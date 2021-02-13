import threading as thread
import queue as q
import time

# Creating a thread locker
print_lock = thread.Lock()

def exampleJob(work):
    """Actual task that is needed to be done."""
    time.sleep(0.5)

    # Applying thread lock on a operation
    with print_lock:
        print(thread.current_thread().name, work)

def threader():
    while True:
        work = que.get()
        exampleJob(work)
        que.task_done()

# Creating a Queue DataStructure
que = q.Queue()

# creating 10 threads
for i in range(10):
    t = thread.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()         # recording start time

# creating task
for work in range(20):
    que.put(work)

#____________queue.join() method_________________#
"""queue.join() blocks until all items in the Queue have been gotten and processed.
The count of unfinished tasks goes up whenever an item is added to the queue.
The count goes down whenever a consumer thread calls task_done() to indicate
the item was retrieved and all work on it is complete.
When the count of unfinished tasks drops to zero, join() unblocks."""
que.join()

print(f'Entire Job took {time.time() - start}')