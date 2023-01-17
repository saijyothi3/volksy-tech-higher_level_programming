#!/usr/bin/python3
"""This module contains a class Square that inherits from Rectangle
    (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle
        (9-rectangle.py)
    Arguments:
        Rectangle (class) -- class
    """

    def __init__(self, size):
        """Instantiation with size.
        Arguments:
            size (int) -- size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
