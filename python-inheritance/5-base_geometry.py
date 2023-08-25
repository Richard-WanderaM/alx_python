#!/usr/bin/env python3
""" Module containing BaseGeometry class """

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

if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("width", 10)
        bg.integer_validator("height", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
