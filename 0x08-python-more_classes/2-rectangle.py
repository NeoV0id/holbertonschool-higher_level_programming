#!/usr/bin/python3
""" Module for rectangle class """


class Rectangle:
    """ class Rectangle """

    def __init__(self, width=0, height=0):
        """
        Init method
        Args:
            width: width
            height: height
        """
        if type(width) is not int:
            raise TypeError("height must be an integer")
        elif (width < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """
        returns rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns rectangle perimeter
        """
        if self.__height or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
