#!/usr/bin/env python3
""" Module containing BaseGeometry and Rectangle classes """

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

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r.__dict__)
