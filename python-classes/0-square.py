#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size):
        self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

