"""Returns string representing list a """


def listToString(a):
    return str(a)


"""Returns picture with a border around it"""


def addBorder(a):
    picture = []
    picture.append('+' + '-'*len(a[0]) + '+')
    for el in a:
        picture.append('|' + el + '|')
    picture.append('+' + '-'*len(a[0]) + '+')
    return picture


"""Returns reductions of strings of list e """


def shorting(e):
    for s in range(len(e)):
        if len(e[s]) > 10:
            e[s] = e[s][0] + str(len(e[s])-2) + e[s][-1]
    return e


"""Returns number of participants who will advance to the next round """


def competition(e, k):
    next_round_participants = 0
    for i in range(len(e)):
        if e[i] != 0 and e[i] >= e[k]:
            next_round_participants += 1
    return next_round_participants


"""Returns sorted list of integers s """


def goodPairs(a, b):
    s = 0
    s2 = []
    for i in a:
        for j in b:
            if (i * j) % (i + j) == 0:
                s = i ** 2 + j ** 2
                s2.append(s)
    return sorted(list(set(s2)))


""" Returns list a of some zeros"""


def makeShell(n):
    a = []
    while len(a) < n:
        a.append([0] * (len(a) + 1))
    while len(a) < (2 * n - 1):
        a.append([0] * (2 * n - len(a) - 1))
    return a


if __name__ == '__main__':
    assert listToString([]) == "[]"
    assert listToString([1, 2, 3]) == "[1, 2, 3]"
    assert listToString([-5]) == "[-5]"

    assert addBorder(['abc',
                      'def']) == ['+---+',
                                  '|abc|',
                                  '|def|',
                                  '+---+']

    assert shorting(['word', 'localization', 'internationalization',
                    'pneumonoultramicroscopicsilicovolcanoconiosis']) == \
        ['word', 'l10n', 'i18n', 'p43s']

    assert competition([5, 4, 3, 2, 1], 2) == 3
    assert competition([1, 0, 0, 0], 3) == 1
    assert competition([10, 9, 8, 7, 7, 7, 5, 5], 4) == 6

    assert goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]) == [128, 160, 180]
    assert goodPairs([2], [2]) == [8]
    assert goodPairs([7, 8, 9], [5, 3, 2]) == []

    assert makeShell(1) == [[0]]
    assert makeShell(2) == [[0], [0, 0], [0]]
    assert makeShell(3) == [[0], [0, 0], [0, 0, 0], [0, 0], [0]]
