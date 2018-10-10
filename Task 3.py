from itertools import tee, count, starmap

"Returns squares of integers in a list"


def squares(a):
    for x in a:
        yield x ** 2


"Returns elements from list elems n times"


def repeatntimes(elems, n):
    for item in tee(elems, n):
        yield from item


"Returns even numbers starting from x"


def evens(x):
    if x % 2 == 0:
        yield from count(x, 2)
    else:
        yield from count(x + 1, 2)


"Returns digits from sequence s"


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


"Returns all symbols of a string with changed case"


def changecase(s):
    return starmap(lambda x: x.swapcase(), s)
