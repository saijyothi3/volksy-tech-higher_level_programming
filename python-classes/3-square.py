#!/usr/bin/python3
"""class"""


class Square:
    """square is size"""

    def __init__(self, size=0):
        """constructor"""
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
            """area of square"""

    return self.__size * self.__size
