#!/usr/bin/python3
"""3-is_kind_of_class.py

    This module contains a function that returns True
    if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance from a_class, or if it inherits from it

        Args:
        obj: Object to check
        a_class (type): class
    """
    return isinstance(obj, a_class)
