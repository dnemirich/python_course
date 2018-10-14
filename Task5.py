"Functions that returns permutations of size n"


def permutations(n):
    def perm_generator(n, prefix=[]):
        if len(prefix) == n:
            yield tuple(prefix)
        else:
            for i in range(1, n + 1):
                if i not in prefix:
                    yield from perm_generator(n, prefix + [i])
    return list(perm_generator(n))


"Function that returns a sequence of n pairs of brackets "


def correctbracketsequences(n):
    def brackets_generator(n, prefix='', balance=0):
        if balance == 0 and len(prefix) == 2 * n:
            yield prefix
        else:
            for i in ('(', ')'):
                new_p = prefix + i
                if i == '(':
                    new_b = balance + 1
                else:
                    new_b = balance - 1
                if len(new_p) <= 2 * n and new_b >= 0:
                    yield from brackets_generator(n, new_p, new_b)
    return list(brackets_generator(n))


"Function that returns all combinations of numbers from n of size k"


def combinationswithrepeats(n, k):
    def comb_generator(n, k, prefix=[]):
        if len(prefix) == k:
            yield tuple(prefix)
        else:
            if len(prefix) == 0:
                start = 1
            else:
                start = max(prefix)
            for i in range(start, n + 1):
                yield from (comb_generator(n, k, prefix + [i]))
    return list(comb_generator(n, k))


"""Function that returns a list of all unsorted partitions of number n as a
sorted tuple of numbers"""


def unorderedpartitions(n):
    def part_generator(n, prefix=[]):
        if sum(prefix) == n:
            yield tuple(prefix)
        else:
            if len(prefix) == 0:
                for i in range(1, n+1):
                    new = prefix + [i]
                    yield from part_generator(n, new)
            else:
                start = prefix[-1]
                for i in range(start, n - start + 2):
                    new = prefix + [i]
                    if sum(new) <= n:
                        yield from part_generator(n, prefix + [i])
    return list(part_generator(n))


if __name__ == '__main__':
    assert permutations(1) == [(1,)]
    assert permutations(2) == [(1, 2), (2, 1)]
    assert permutations(3) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1),
                               (3, 1, 2), (3, 2, 1)]
    print("permutations function - OK")

    assert combinationswithrepeats(1, 1) == [(1,)]
    assert combinationswithrepeats(2, 2) == [(1, 1), (1, 2), (2, 2)]
    assert combinationswithrepeats(3, 2) == [(1, 1), (1, 2), (1, 3), (2, 2),
                                             (2, 3), (3, 3)]
    print("combinationswithrepeats function - OK")

    assert unorderedpartitions(1) == [(1,)]
    assert unorderedpartitions(3) == [(1, 1, 1), (1, 2), (3,)]
    assert unorderedpartitions(5) == [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 3),
                                      (1, 2, 2), (1, 4), (2, 3), (5,)]
    print("unorderedpartitions function - OK")

    assert correctbracketsequences(1) == ['()']
    assert correctbracketsequences(2) == ['(())', '()()']
    assert correctbracketsequences(3) == ['((()))', '(()())', '(())()',
                                          '()(())', '()()()']
    print("correctbracketsequences function - OK")
