# Question 

# Update the class Rectangle by updating the public method def update(self, *args):
#  by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

# **kwargs can be thought of as a double pointer to a dictionary: key/value
# As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
# **kwargs must be skipped if *args exists and is not empty
# Each key in this dictionary represents an attribute to the instance
# This type of argument is called a “key-worded argument”. Argument order is not important.


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

    def update(self, *args, **kwargs):
        """ Update attributes using *args and **kwargs """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

if __name__ == "__main__":
    """ Test cases """
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)


# Solution Explained

# The update method is updated to accept both *args and **kwargs.
#  It first checks if args is present.
#  If so, it assigns values to attributes in the order of id, width, height, x, and y.

# If no args are provided, the method checks for the presence of kwargs (key-value arguments).
#  It then iterates through the key-value pairs in kwargs,
#  and assigns values to the corresponding attributes using the setattr function.

# The provided test cases in the 8-main.py script create an instance of the Rectangle class,
#  and call the update method with both args and kwargs,
#  to demonstrate how attributes can be updated using both approaches.