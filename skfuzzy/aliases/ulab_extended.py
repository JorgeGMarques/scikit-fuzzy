
"""
ulab_extended.py : Various partially implemented numpy methods that are not
                    shipped with ulab.
"""

from ulab import numpy as np

def hstack(a,b):
    """
    Stack 1-D 2-D arrays in sequence horizontally (column wise).

    Parameters
    ----------
    a : 2d array (C, N)
    b : 2d array (C, N)

    Returns
    -------
    Horizontal stacked array
    """

    a = _atleast_2d(a)
    b = _atleast_2d(b)

    ra, ca = a.shape
    rb, cb = b.shape

    _hstack = np.zeros((max(ra,rb), ca+cb))

    for i in range(0, max(ra,rb)):
        for j in range(0, ca+cb):
            if j < ca:
                _hstack[i][j] = a[i][j] if i < ra else 0
            else:
                _hstack[i][j] = b[i][j-ca] if i < rb else 0
    return _hstack


def vstack(a,b):
    """
    Stack 1-D or 2-D arrays in sequence vertically (row wise).

    Parameters
    ----------
    a : 2d array (C, N)
    b : 2d array (C, N)

    Returns
    -------
    Vertical stacked array
    """

    a = _atleast_2d(a)
    b = _atleast_2d(b)

    ra, ca = a.shape
    rb, cb = b.shape

    _vstack = np.zeros((ra+rb, max(ca,cb)))

    for i in range(0, ra + rb):
        for j in range(0, max(ca,cb)):
            if i < ra:
                _vstack[i][j] = a[i][j] if j < ca else 0
            else:
                _vstack[i][j] = b[i-ra][j] if j < cb else 0
    return _vstack


def atleast_2d(x):
    """
    Returns atleast 2d array

    Parameters
    ----------
    x : array

    Returns
    -------
    x : at least 2d array
    """
    if (hasattr(x, 'shape')):
        l = x.shape
        if len(l) == 0 or len(l) == 1:
            return np.array([x])
        else:
            return x
    else:
        return np.array([[x]])

def nonzero(a, op, b):
    """
    Return a turple with 1 dimesion numpy array with the indices corresponding
    to the elements that match the condition.

    Parameters
    ----------
    a : 1d array
        Fuzzy membership sequence.
    op : string
        Comparation operator.
    b : float
        Value used for comparation.

    Returns
    -------
    nonzero : 1d array inside turple
        Indices corresponding to the elements that match the condition
    """
    _where = {
        '<=': np.where(a <= b, 1, 0),
        '==': np.where(a == b, 1, 0),
        '>=': np.where(a >= b, 1, 0),
        '<' : np.where(a <  b, 1, 0),
        '>' : np.where(a >  b, 1, 0)
    }[op]
    _nonzero = []
    for i in range(0, a.size):
        if (_where[i] == 1):
            _nonzero.append(i)
    return (np.array(_nonzero),)


def ravel(a):
    """
    A 1-D array, containing the elements of the input, is returned.

    Parameters
    ----------
    a : 2d array
        Input array. The elements in a are read in the order specified by order, and packed as a 1-D array.

    Returns
    -------
    y : 1d array
        An array of the same subtype as a, with shape (a.size,).
    """
    (r,c) = a.shape

    y = np.zeros(a.size)
    for i in range(0, r):
        y[c*i:c*(i+1)] = a[i]

    return y


def unique(a):
    """
    Find the unique elements of an array.

    Parameters
    ----------
    a : 1d or 2d array
        Input array. This will be flattened if it is not already 1-D.

    Returns
    -------
    unique : The sorted unique values.

    """

    if (len(a.shape) == 2):
        a = ravel(a)

    _u = []

    y = np.zeros(a.size)
    for i in range(0, a.size):
        if not a[i] in _u:
            _u.append(a[i])

    unique = np.array(_u)
    unique.sort()

    return unique


def logical_and(x1,x2):
    """
    Compute the truth value of x1 AND x2 element-wise.

    Parameters
    ----------
    x1, x2: 1d array

    Returns
    -------
    y : 1d array
        Boolean result of the logical AND operation applied to the elements
        of x1 and x2.
    """

    y = np.zeros(x.size)

    for i  in range(0, x.size):
        y[i] = 1 if x[i] == 1 and y[i] == 1 else 0

    return y
