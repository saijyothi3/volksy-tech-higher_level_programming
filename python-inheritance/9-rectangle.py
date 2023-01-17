#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
        (7-base_geometry.py).
    Arguments:
        BaseGeometry (cls) -- class
    """

    def __init__(self, width, height):
        """Instantiation with width and height.
        Arguments:
            width (int) -- width.
            height (int) -- height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Returns the following rectangle description:
            [Rectangle] <width>/<height>
        Returns:
            str -- [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns a rectangle area.
        Returns:
            int -- rectangle area.
        """
        return self.__width * self.__height
