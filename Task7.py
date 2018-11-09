import socket


def valuesunion(*dicts):
    s = []
    for dict in dicts:
        s += dict.values()
    return set(s)


def popcount(n):
    a = str(bin(n))
    return a.count('1')


def powers(n, m):
    d = {i: i ** i % m for i in range(1, n + 1)}
    return d


def isIPv4(s):
    try:
        socket.inet_aton(s)
    except socket.error:
        return False
    return True


def pascals(n, p=[]):
    for x in range(n):
        L = len(p)
        p = [1 if i == 0 or i == L else p[i - 1] + p[i] for i in range(L + 1)]
        yield tuple(p)
