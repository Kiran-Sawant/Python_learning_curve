import datetime as dt
n = 2

t1 = "Sat 24 Mar 2170 03:47:07 +0430"
t2 = "Mon 30 Dec 2272 20:27:41 -1000"
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000

# listx = s.split('\n')

# Creatign datetime objects using formatted string.
k1 = dt.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
k2 = dt.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

delta = k1 - k2
print(int(delta.total_seconds()))