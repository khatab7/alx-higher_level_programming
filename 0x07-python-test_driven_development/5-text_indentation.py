#!/usr/bin/python3
"""Module built for Python 0x07 task 4. Error in project formatting scheme \
advances file numbering +1 for every task after 0.
"""


def text_indentation(text):
    """Indent the given text based on specified delimiters.

    Args:
        text (str): Text to be indented.

    Raises:
        TypeError: If the input is not a string.

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    delimiters = '.?:'

    for delimiter in delimiters:
        text = text.replace(delimiter, delimiter + ' ')

    words = text.split()

    for i, word in enumerate(words):
        if word.endswith(('.', '?', ':')):
            print(word, end='\n\n')
        elif i == len(words) - 1:
            print(word, end='')
        else:
            print(word, end=' ')
