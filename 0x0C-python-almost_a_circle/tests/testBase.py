#!/usr/bin/python3
"""
Base/Rectangle/Square tests
"""



from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""
Test Base 1:
    testing creation of form for Base
"""
form1 = Base(id = 8)
form2 = Base(id = None)
print(form1.id, form2.id)


"""
Test Rectangle 1:
    testing creation of rectangle from Rectangle
"""
rec1 = Rectangle(id=None, width=8, height=4, x=5, y=5)
print(rec1.width, rec1.height, rec1.x, rec1.y)

"""
Test Rectangle 2:
    testing creation of rectangle from Rectangle
"""
rec1 = Rectangle(id=None, width=8, height=4, x=7, y=5)
print(rec1.id, rec1.width, rec1.height, rec1.x, rec1.y)

"""
Test Rectangle 3:
    testing display method
"""
rec2 = Rectangle(id=5, width=10, height=5, x=7, y=8)
rec2.display()

"""
Test Rectangle 4:
    testing area method
"""
print(rec.area())

"""
Test Square 1:
    testing square creation
"""
sq = Square(4, 4, 3, 1)

"""
Test Square 2:
    testing display and area methods
"""
sq.display()
sq.area()

"""
Test handling errors:
    0 for x in square
    0 for size in square
    negative numbers in square
    0 for both height and width in rectangle
    display 0 sized rectangle
"""
sq1 = Square(4, 4, 0, 1)
sq2 = Square(2, 0, 7, 2)
sq3 = Square(2, 8, 7, -2)
sq4 = Square(2, 8, -5, -2)
rec = Square(0, 0, 5, 2)
rec.display()

