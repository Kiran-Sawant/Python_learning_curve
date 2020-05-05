def oddy():
    start = 1
    while True:
        yield start
        start += 2
    

def pi_series():
    odds = oddy()
    approx = 0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx

approx_pi = pi_series()

for i in range(1000):
    print(next(approx_pi))
