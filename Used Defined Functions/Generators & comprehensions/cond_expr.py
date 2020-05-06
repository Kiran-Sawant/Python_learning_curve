for x in range(1, 31):
    # Using conditional expression
    fizzbuzz = 'fizz buzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
    print(fizzbuzz)