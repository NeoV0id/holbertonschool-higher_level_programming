#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method
        Args:
            size: size of the square
            width: width
            height: height
            x: x
            y: y
            id: the id inherited from rectangle
        """
        super().__init__(size, size, x, y, id)
        if (type(size) != int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__size = size
            width = size
            height = size

    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size> -
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        size setter
        """
        if (type(size) != int):
            raise TypeError("width must be an integer")
        elif (size <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__size = size
            width = size
            height = size

    def update(self, *args, **kwargs):
        """
        public method
        """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == "id":
                        self.id = kwargs["id"]
                    if i == "size":
                        self.size = kwargs["size"]
                    if i == "x":
                        self.x = kwargs["x"]
                    if i == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
