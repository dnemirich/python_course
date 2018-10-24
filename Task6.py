Task 6

Common description

Your implementations should use numpy library.

All of this functions can be implemented using one line of code with calling function from numpy.

All examples below are written with the following import:

    import numpy as np

Sometimes your result can be equal to correct result with some precision (e.g. 122.999999994 instead of 123). It is ok.
Description of arguments

Arguments a and b are np.array. They can have any dimension if there are no remarks in description of function.

Arguments n and k are int.

Other arguments can be int and float.
Description of functions

    def getdimension(a):

    Return dimension of array a

    For example:

    getdimension(np.array([1, 2, 3])) = 1
    getdimension(np.array([[1], [2], [3]])) = 2
    getdimension(np.array([[[[1]]]])) = 4

    def getdiagonal(a):

    a is 2-dimensional square array (number of rows is equal to number of columns). Find its diagonal.

    For example:

    getdiagonal(np.array([[1, 2], [3, 4]])) = np.array([1, 3])

    def cutarray(a, minvalue, maxvalue):

    Return copy of array a with some values replaces:
        If entry x is less than minvalue, replace it with minvalue
        If entry x is greater than maxvalue, replace it with maxvalue
        Otherwise you should not replace it.

    For example:

    cutarray(np.array([1, 2, 3, 4]), 2, 3) = np.array([2, 2, 3, 3])

    def getmoments(a):

    Return tuple with two values:
        Mean value of entries of a
        Variance of entries of a

    For example:

    getmoments(np.array([2, 1, 9])) = (12.666666666666666, 3.5590260840104371)

    def getdotproduct(a, b):

    a and b vectors represented by 1-dimensional arrays with the same length. Return dot product of this vectors.

    For example:

    getdotproduct(np.array([1, 2, 3]), np.array([4, 5, 6])) = 32

    def checkequal(a, b):

    a and b are arrays of the same shape. Return matrix of the same shape as a and b such that entry of result is True if corresponding elements of a and b are equal or False otherwise.

    For example:

    checkequal(np.array([1, 2, 3]), np.array([1, 5, 3])) = np.array([True, False, True])

    def comparewithnumber(a, bound):

    Return matrix of the same shape as a such that element of the result is True if corresponding element of a is less than bound and False otherwise.

    For example:

    comparewithnumber(np.array([[1, 2], [3, 4]]), 4) = np.array([[True, True], [True, False]])

    def matrixproduct(a, b):

    a and b are 2-dimensional arrays of the same shape. Return the product of matrices represented by these arrays.

    For example:

    matrixproduct(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])) = np.array([[19, 22], [43, 50]])

    def matrixdet(a):

    a is square 2-dimensional array. Find determinant of the matrix represented by this array.

    For example:

    matrixdet(np.array([[5, 6], [7, 8]])) = -2
    matrixdet(np.array([[123]])) = 123

    def getones(n, k):

    Return 2-dimensional array of shape (n, n) such that entry with indices (i, j) (i is index of row, j is index of column) is equal to:
        1.0 if j - i = k
        0.0 otherwise

    For example:

    getones(3, 1) = np.array([[0., 1., 0.],
                              [0., 0., 1.],
                              [0., 0., 0.]])
    getones(3, 9) = np.array([[0., 0., 0.],
                              [0., 0., 0.],
                              [0., 0., 0.]])
