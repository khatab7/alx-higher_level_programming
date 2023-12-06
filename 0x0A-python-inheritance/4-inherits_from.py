#!/usr/bin/python3
""" 4-inherits_from.py
    This module cntains a function that returns True if the object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Checks if obj inherits from a_class"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
