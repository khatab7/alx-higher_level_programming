#!/usr/bin/python3
"""Module 2-matrix_divided.

This module contains the function matrix_divided that divides all the
elements of a matrix by a divisor.

"""


from typing import List

def matrix_divided(matrix: List[List[float]], div: float) -> List[List[float]]:
    """
    Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix (List[List[float]]): The matrix to be divided.
        div (float): The divisor.
    
    Returns:
        List[List[float]]: A new matrix with the divided values.
    
    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
        TypeError: If each row of the matrix does not have the same size.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
