#!/usr/bin/env python3
""" Module containing BaseGeometry class """

class BaseGeometry:
    """ Class representing a basic geometry shape """

    def area(self):
        """ Calculate the area of the geometry shape """
        raise Exception("area() is not implemented")

if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
