#!/usr/bin/python3
"""Module built for Python 0x07 task 2. Error in project formatting scheme \
advances file numbering +1 for every task after 0.
"""


def say_my_name(first_name, last_name=""):
    """Function that prints "My name is ", followed by the one or two string \
arguments given.

    Args:
        first_name (str): string representing first name
        last_name (str): string representing last name

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
