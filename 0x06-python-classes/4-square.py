#!/usr/bin/python3
""" module for class square """

class Square:
    """ Square: define a square
        Attributes:
            width (int): size (height and width) of the square
    """
    def __init__(self, size=0):
        """ __init__ : initialisation of Square class
            Args:
                size (int): size (height and width) of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        return
        @property
        def size(self):
            """ size: get size of object square
                Args:
                    none
                Returns: size
            """
            return self.__size
    
        @size.setter
        def size(self, size):
            """ size: get size of object square
                Args:
                    size (int): square size, must be int
            """
            try:
                self.__size = size
                if (type(size) != int):
                    raise TypeError
                elif (size < 0):
                    raise ValueError
            except TypeError:
                print("size must be an integer")
            except ValueError:
                print("size must be >= 0")
    def area(self):
        """
        Instance method
        Returns:
            the current square area
        """
        return(self.__size ** 2)
