#!/usr/bin/python3
"""0-lookup.py
This module contains a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """lookup - Returns methods and attributes of a python object

    Args:
        obj: Python object

    Returns:
        (list): List of methods/attributes of obj
    """
    return dir(obj)
