#!/usr/bin/python3
""" module for class rectangle """


class Rectangle:
    """ Rectangle: define a rectangle
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """ __init__ : initialisation of Square class
            Args:
                width (int): width  of the rectangle
                height (int): height of the rectangle
        """
        @property
        def width(self):
            """ width: get width of object rectangle
                Args:
                    none
                Returns: width
            """
            return self.__width

        @width.setter
        def width(self, width):
            """ width: get size of object square
                Args:
                    width (int): rectangle width, must be int
            """
            try:
                self.__width = width
                if (type(width) != int):
                    raise TypeError
                elif (width < 0):
                    raise ValueError
            except TypeError:
                print("width must be an integer")
            except ValueError:
                print("width must be >= 0")
        
        @property
        def height(self):
            """ height: get height of object rectangle
                Args:
                    none
                Returns: height
            """
            return self.__height

        @height.setter
        def height(self, height):
            """ height: get size of object square
                Args:
                    height (int): rectangle height, must be int
            """
            try:
                self.__height = height
                if (type(height) != int):
                    raise TypeError
                elif (height < 0):
                    raise ValueError
            except TypeError:
                print("height must be an integer")
            except ValueError:
                print("height must be >= 0")
