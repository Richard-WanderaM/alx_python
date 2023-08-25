#!/usr/bin/python3

"""
This module defines a Square class that represents a square by its size.
"""

class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.
        """
        self.__size = size

# Testing the Square class
if __name__ == "__main__":
    my_square = Square(5)
    print(my_square.__dict__)



