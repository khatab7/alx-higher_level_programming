#!/usr/bin/python3
"""Module for 0x07
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of int or float): First matrix.
        m_b (list of lists of int or float): Second matrix.

    Returns:
        list of lists of int or float: Resulting matrix.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list or contains elements that are not lists.
        ValueError: If `m_a` or `m_b` is empty or contains rows of unequal lengths.
        TypeError: If `m_a` or `m_b` contains elements that are not integers or floats.
        ValueError: If the number of columns in `m_a` is not equal to the number of rows in `m_b`.

    """

    # Check type and structure of matrices
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')

    # Check for empty matrices
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't contain empty rows")
    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't contain empty rows")

    # Check element types of matrices
    for row in m_a:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    # Check for rectangular matrices
    row_len = len(m_a[0])
    for row in m_a:
        if len(row) != row_len:
            raise ValueError('each row of m_a must have the same length')

    row_len = len(m_b[0])
    for row in m_b:
        if len(row) != row_len:
            raise ValueError('each row of m_b must have the same length')

    # Check dimensions for matrix multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    new_matrix = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            new_row.append(sum)
        new_matrix.append(new_row)

    return new_matrix
