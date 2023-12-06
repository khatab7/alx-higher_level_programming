#!/usr/bin/python3
"""6-base_geometry.py

This module contains a class BaseGeometry (based on 5-base_geometry.py):

    - Public instance method: def area(self): that raises an Exception with
        the message 'area() is not implemented'
"""


class BaseGeometry():
    """Base geometry methods/atributes"""
    def __init__(self):
        """ Sets attributes for a BaseGeometry object when it's instanciated"""
        pass

    def area(self):
        """Method to get area of an object. Not yet implemented"""
        raise Exception("area() is not implemented")
