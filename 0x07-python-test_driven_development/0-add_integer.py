#!/usr/bin/python3
"""Module built for 0x07.
"""

def add_integer(a: float or int, b: float or int = 98) -> int:
    """Function that adds two integers.

    Args:
        a (float or int): First argument to add to the sum.
        b (float or int, optional): Second argument to add to the sum. Defaults to 98.

    Returns:
        int: Sum of the two values.

    Raises:
        TypeError: If either argument is not an integer or a float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or a float')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or a float')

    return int(a) + int(b)
