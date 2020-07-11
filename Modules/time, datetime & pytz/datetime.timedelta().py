import datetime as dt

""" Timedelta Represent the difference between two datetime objects.

    Supported operators:

    - add, subtract timedelta
    - unary plus, minus, abs
    - compare to timedelta
    - multiply, divide by int

    In addition, datetime supports subtraction of two datetime objects
    returning a timedelta, and addition or subtraction of a datetime
    and a timedelta giving a datetime.

    Representation: (days, seconds, microseconds, milliseconds, minutes, hours, weeks).
    """

# Getting Current time.
cur_time = dt.datetime.now()

# Creating a time Delta of 5 hours.
delta = dt.timedelta(hours=5)
# adding current time to delta.
five_h = cur_time + delta

# Creating a timedelta of 300 min (5 hrs)
delta2 = dt.timedelta(minutes=300)
# Adding 300 minutes(5 hrs) to current time.
five_h = cur_time + delta2

# Creting a delta of 8 hrs, 15 min & 30 seconds.
delta3 = dt.timedelta(hours=8, minutes=15, seconds=30)
future_time = cur_time + delta3

print(future_time)