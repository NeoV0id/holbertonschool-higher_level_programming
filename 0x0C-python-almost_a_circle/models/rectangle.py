#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init method
        Args:
            width: width
            height: height
            x: x
            y: y
            id: id(base)
        """
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if (type(x) != int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if (type(y) != int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, n):
        """
        width setter
        """
        try:
            self.__width = width
        except TypeError as err1:
            print("width must be an integer")
        except ValueError as err2:
            print("width must be > 0")

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, n):
        """
        height setter
        """
        try:
            self.__height = n
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be > 0")

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, n):
        """
        x setter
        """
        try:
            self.__x = n
        except TypeError:
            print("x must be an integer")
        except ValueError:
            print("x must be >= 0")

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, n):
        """
        y setter
        """
        try:
            self.__y = n
        except TypeError:
            print("y must be an integer")
        except ValueError:
            print("y must be >= 0")

    def area(self):
        """
        returns rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
        display rectangle
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        initialize arguments
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
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
                    if i == "width":
                        self.width = kwargs["width"]
                    if i == "height":
                        self.height = kwargs["height"]
                    if i == "x":
                        self.x = kwargs["x"]
                    if i == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns Rectangle as dictionnary
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
