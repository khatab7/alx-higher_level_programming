#!/usr/bin/python3
"""100-my_int.py

This module contains a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """Defines an int with inverted == and != operators"""

    def __eq__(self, obj):
        """Turns '==' operator into '!=' """
        return int(self) != int(obj)

    def __ne__(self, obj):
        """Turns '!=' operator into '==' """
        return int(self) == int(obj)
