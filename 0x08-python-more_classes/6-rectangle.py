#!/usr/bin/python3
""" Module for rectangle class """


class Rectangle:
    """ class Rectangle """

    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        display rectangle
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __print__(self):
        """
        display rectangle
        """
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            print("")

    def __repr__(self):
        """
        return string representation of a string
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        print 'Bye Rectangle' when an istance of a Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye Rectangle...")
