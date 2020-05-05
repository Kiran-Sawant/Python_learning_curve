#_______Calculating Factorial________#
def fact(n):
    result = 1
    if n > 1:
        for i in range(2, n + 1):
            result *= i
    return result

#______Calculating factorial recursively_____#
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

#______calculating fibonacchi_______#
def fib(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n + 1):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

#______calculating fibonacci recursively___#
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


for i in range(6):
    print(i, fibonacci(i))