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
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# Testing the Square class
if __name__ == "__main__":
    try:
        my_square = Square(5)
        print(my_square.__dict__)
        print("Area:", my_square.area())
        my_square.my_print()

        my_square.size = 3
        print("New size:", my_square.size)
        my_square.my_print()
        
        empty_square = Square()
        empty_square.my_print()
        
        invalid_square = Square("not_an_integer")
    except Exception as e:
        print(e)
