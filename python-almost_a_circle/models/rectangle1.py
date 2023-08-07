# Question

# Write the class Rectangle that inherits from Base:

# In the file models/rectangle.py
# Class Rectangle inherits from Base
# Private instance attributes, each with its own public getter and setter:
# __width -> width
# __height -> height
# __x -> x
# __y -> y
# Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
# Call the super class with id - this super call with use the logic of the __init__ of the Base class
# Assign each argument width, height, x and y to the right attribute
# Why private attributes with getter/setter? Why not directly public attribute?

# Because we want to protect attributes of our class. 
# With a setter, you are able to validate what a developer is trying to assign to a variable.
#  So after, in your class you can “trust” these attributes.

#!/usr/bin/python3
""" Rectangle module """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class, inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.__y = value

if __name__ == "__main__":
    """ Test cases """
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)


# Explanation

# The Rectangle class is defined, inheriting from the Base class.

# The constructor method __init__ is defined.
# It takes the arguments width, height, x, y, and id.
#  It calls the constructor of the parent class (Base) using super().__init__(id) and,
#  then assigns the provided arguments to the corresponding private instance attributes.

# Getter and setter methods are defined for each of the private instance attributes (width, height, x, and y).
#  These methods are used to control access to these attributes and provide a layer of validation and protection.

# The if __name__ == "__main__": block contains test cases to demonstrate the behavior of the Rectangle class.