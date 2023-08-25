#!/usr/bin/env python3
""" Module containing BaseGeometry, Rectangle, and Square classes """

class BaseGeometry:
    """ Class representing a basic geometry shape """

    def area(self):
        """ Calculate the area of the geometry shape """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate an integer value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Class representing a rectangle """

    def __init__(self, width, height):
        """ Initialize a rectangle with width and height """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Return the string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

class Square(Rectangle):
    """ Class representing a square """

    def __init__(self, size):
        """ Initialize a square with a size """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Return the string representation of the square """
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
