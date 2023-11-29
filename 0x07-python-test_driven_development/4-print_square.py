#!/usr/bin/python3
"""A Module built for 0x07
"""

def print_square(size: int) -> None:
    """Function that prints a square of a given size in '#' characters.

    Args:
        size (int): Length of the side of the square, in monospace characters.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size)
