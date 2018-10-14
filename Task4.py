"Returns factorial of a number n"


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


"Returns n-th Fibonacci sequence number"


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


"Returns the sum of digits of number n"


def digitsum(n):
    if n // 10 == 0:
        return n
    return n % 10 + digitsum(n // 10)


"Returns Ackermann number"


def ackermann(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


"Returns a greatest common multiple of a and b"


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
