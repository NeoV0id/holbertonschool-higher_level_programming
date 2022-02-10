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
            size(int): size of the square
            x(int): x
            y(int): y
            id(int): the id inherited from rectangle
        """
        super().__init__(size, size, x, y, id)

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
        return self.size

    @size.setter
    def size(self, size):
        """ size: get size of object square
            Args:
                size (int): square size, must be int
        """
        try:
            if (type(size) != int):
                raise TypeError
            elif (size <= 0):
                raise ValueError
            else:
                self.__size = size
                width = size
                height = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be > 0")

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
