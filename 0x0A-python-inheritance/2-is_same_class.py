#!/usr/bin/python3
"""2-is_same_class.py

    This module contains a function that returns True
    if the object is exactly an instance of the specified class;
    otherwise False.
"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class

    Args:
        obj (_type_): object
        a_class (type): class

    Returns:
        (bool): True if it is and instance of the class, False otherwise
    """
    return type(obj) is a_class
