# Question

# Update the class Rectangle by adding the public method def update(self, *args):
#  that assigns an argument to each attribute:

# 1st argument should be the id attribute
# 2nd argument should be the width attribute
# 3rd argument should be the height attribute
# 4th argument should be the x attribute
# 5th argument should be the y attribute

# This type of argument is called a “no-keyword argument” - Argument order is super important.


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

    def display(self):
        """ Display the rectangle using # characters """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ String representation of the object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """ Update attributes using *args """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)

if __name__ == "__main__":
    """ Test cases """
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)


# My code solution explained

# The update method takes a variable number of arguments *args.
#  It iterates over the provided arguments and assigns them to the corresponding attributes;
#  (id, width, height, x, y) using the setattr function.

# The provided test cases in the 7-main.py script create an instance of the Rectangle class,
#  and call the update method with different sets of arguments,
#  to demonstrate how the attributes can be updated using this method.