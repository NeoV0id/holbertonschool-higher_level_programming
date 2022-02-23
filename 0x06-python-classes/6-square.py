#!/usr/bin/python3
""" module for class square """


class Square:
    """ Square: define a square
        Attributes:
            width (int): size (height and width) of the square
    """
    def __init__(self, size=0, position):
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
        self.__position = position

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
        """ 
            size: get size of object square
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

    @property
    def position(self):
        """
            position getter
            Args:
                None
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            position setter
            Args:
                value: is the position
        """
        try:
            self.__position = value
            if (type(value) != tuple and type(value) != int):
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """
            Instance method
            Returns:
                the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
            Instance method
            Returns:
                the printed square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                if position[1] > 0:
                    continue
                else:
                    for n in range(0, self.__position + 1):
                        print(" ")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
