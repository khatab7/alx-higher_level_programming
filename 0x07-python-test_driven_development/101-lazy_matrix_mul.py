#!/usr/bin/python3
"""Module built for 0x07"""

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: Result of matrix multiplication.

    Raises:
        ValueError: If matrices are not compatible for multiplication.

    """
    import numpy as np

    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError:
        raise ValueError("Matrices are not compatible for multiplication.")
