"""The queue module implements multi-producer, multi-consumer queues.
It is especially useful in Multi-threaded programming when information
must be exchanged safely between multiple threads. The Queue class in
this module implements all the required locking semantics.
    The module implements three types of queue, which differ only in
the order in which the entries are retrieved. In a FIFO queue, the
first tasks added are the first retrieved. In a LIFO queue, the most
recently added entry is the first retrieved (operating like a stack).
With a priority queue, the entries are kept sorted and the lowest
valued entry is retrieved first.
    Internally, those three types of queues use locks to temporarily
block competing threads; however, they are not designed to handle
reentrancy within a thread.
Full Doc: https://docs.python.org/3/library/queue.html"""

from queue import Queue
import queue

# Creating an empty Queue object.
"""maxsize determines max number of items that can possibally be
inserted. 0(default) or < 0 means Infinite."""
q = Queue(maxsize=0)

# Populating the Queue Object.
for i in range(20):
    """.put() method inserts items into queue, allowing only one
    thread at a time"""
    q.put(i, block=True)
    # q.put_nowait(i)               #

# .qsize() returns number of items in the queue.
print(f"Queue size: {q.qsize()}")

# .full() returns True if max size reached.
print(f"Queue full: {q.full()}")

# poping out the values in the Queue.
for i in range(q.qsize()):
    """.get() pops items from the queue in a FIFO manner"""
    print(f"Popping out: {q.get(block=True)}")
    # print(f"Popping out: {q.get_nowait()}")               # equivalent to block=False

# The size will be 0 as all items are popped.
print(f"Queue size: {q.qsize()}")

# Returns True if Queue is empty.
print(f"Queue Empty: {q.empty()}")

#_______ .task_done()__________#
"""As queue module has internal thread-locking mechanisms that
makes it very useful in Multi-threaded applications that
may use daemonic threads.
    .task_done() is placed after the work is done indicating the
work is done and when there are no tasks left the code can move
beyond .join() method that blocks the code."""
q.task_done()

#__________ .join() method____________#
"""Blocks until all items in the queue have been gotten and processed.
The count of unfinished tasks goes up whenever an item is added to the
queue. The count goes down whenever a consumer thread calls task_done()
to indicate that the item was retrieved and all work on it is complete.
When the count of unfinished tasks drops to zero, join() unblocks."""
q.join()