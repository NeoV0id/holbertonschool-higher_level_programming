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
            number_of_instances: count the number of object created
        """
        number_of_instances = 0
        print_symbol = "#"

        self.__width = width
        self.__height = height
        number_of_instances += 1

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

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
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter

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
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __repr__(self):
        """
        return string representation of a string
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        print 'Bye Rectangle' when an istance of a Rectangle is deleted
        """
        number_of_instances -= 1
        print("Bye Rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1 is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif rect_2 is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area < rect_2.area():
                return rect_2
            else:
                return rect_1
