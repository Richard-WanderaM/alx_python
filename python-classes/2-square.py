#!/usr/bin/python3

"""
This module defines a Square class that represents a square by its size.
"""

class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes a square with an optional size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

# Testing the Square class
if __name__ == "__main__":
    try:
        my_square = Square(5)
        print(my_square.__dict__)
        print("Area:", my_square.area())
        
        invalid_square = Square("not_an_integer")
    except Exception as e:
        print(e)
