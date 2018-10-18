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


"Returns reversed string s"


def reversestring(s):
    if len(s) <= 1:
        return s
    return s[-1] + reversestring(s[0:-1])


"Returns a True if n is a 2 to some power"


def istwopower(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return istwopower(n // 2)
    return False


"Returns list of all binary strings of lenght n"


def genbinarystrings(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1']
    list = []
    for i in genbinarystrings(1):
        for j in genbinarystrings(n - 1):
            list.append(i + j)
    return list


"""Returns an integer that is equal to a decimal representation of concatenated
a and b"""


def concatnumbers(a, b):
    if b // 10 == 0:
        return a * 10 + b
    return concatnumbers(a, b // 10) * 10 + b % 10


"Returns string s with parentheses"


def parentheses(s):
    if len(s) <= 2:
        return '(' + s + ')'
    return '(' + s[0] + parentheses(s[1: -2 + 1]) + s[-1] + ')'


"""Returns palyndrom that increases in first part from 1 to n and decreases in
the second part from n to 1"""


def abacaba(n):
    if n == 1:
        return [1]
    return abacaba(n - 1) + [n] + abacaba(n - 1)
