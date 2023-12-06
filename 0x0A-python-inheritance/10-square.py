#!/usr/bin/python3
"""The module Square inherits from Rectangle which inherits from BaseGeometry
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square. Inherits from class Rectangle"""

    def __init__(self, size):
        """Initializes a Square object when it is instanciated"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of the Square object"""
        return self.__size ** 2
