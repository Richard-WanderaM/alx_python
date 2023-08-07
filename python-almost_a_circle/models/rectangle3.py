# Question

# Update the class Rectangle by adding the public method def area(self):
#  that returns the area value of the Rectangle instance.

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

if __name__ == "__main__":
    """ Test cases """
    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())


# Solution Explanation

# The area method is added to the Rectangle class.
#  It calculates the area by multiplying the width and height of the rectangle.

# The provided test cases in the 3-main.py script create instances of the Rectangle class,
#  and call the area method to calculate and print the area of each rectangle.