"""This function should return sorted list of distinct elements of e"""


def unique(e):
    e = list(set(e))
    return(sorted(e))


"""This function should return transposed dict d.
It is garantueed that all the values of dict d are distinct"""


def transposeDict(d):
    return {key: value for (value, key) in d.items()}


"""This function should return minimal positive integer
which is not present at list e"""


def mex(e):
    return min([i for i in range(1, len(e)+5) if i not in e])


"""This function should return dict with counts of every symbol
from string s"""


def frequencyDict(s):
    return {el: s.count(el) for el in s}


if __name__ == '__main__':
    assert unique([1, 2, 1, 3]) == [1, 2, 3]
    assert unique({5, 1, 3}) == [1, 3, 5]
    assert unique('adsfasdf') == ['a', 'd', 'f', 's']

    assert transposeDict({1: 'a', 2: 'b'}) = {'a': 1, 'b': 2}
    assert transposeDict({1: 1}) = {1: 1}
    assert transposeDict({}) = {}

    assert mex([1, 2, 3]) = 4
    assert mex(['asdf', 123]) = 1
    assert mex([0, 0, 1, 0]) = 2

    assert frequencyDict('') = {}
    assert frequencyDict('abacaba') = {'a': 4, 'b': 2, 'c': 1}
