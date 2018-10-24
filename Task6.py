"Task 6"


import numpy as np


"Returns a dimension of an array a"


def getdimension(a):
    return a.ndim


"Returns a diagonal of a (2-dimensional array)"


def getdiagonal(a):
    return np.diagonal(a)


"Returns a copy of an array a with some value replaces"


def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


"Returns a tuple with 2 values: mean value and variance"


def getmoments(a):
    return np.mean(a), np.var(a)


"Returns a dot product of vectors a and b"


def getdotproduct(a, b):
    return np.dot(a, b)


"Returns a matrix of Booleans, if elements in a and b are corresponding"


def checkequal(a, b):
    return np.equal(a, b)


"Returns a matrix of Booleans, True if the element in matrix a less than bound"


def comparewithnumber(a, bound):
    return a < bound


"Returns the product of matrices a and b "


def matrixproduct(a, b):
    return a @ b


"Returns a determinant of a matrix"


def matrixdet(a):
    return np.linalg.det(a)


"Returns a 2-D array with ones on the diagonal and zeros elsewhere, diagonal-k"


def getones(n, k):
    return np.eye(n, k=k, dtype=int)
