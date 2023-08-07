# Question

# Write the class Square that inherits from Rectangle:

# In the file models/square.py
# Class Square inherits from Rectangle
# Class constructor: def __init__(self, size, x=0, y=0, id=None)::
# Call the super class with id, x, y, width and height -
#  this super call will use the logic of the __init__ of the Rectangle class.
#  The width and height must be assigned to the value of size

# You must not create new attributes for this class, use all attributes of Rectangle
#  - As reminder: a Square is a Rectangle with the same width and height

# All width, height, x and y validation must inherit from Rectangle
#  - same behavior in case of wrong data

# The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height

# As you know, a Square is a special Rectangle,
#  so it makes sense this class Square inherits from Rectangle.
#  Now you have a Square class who has the same attributes and same methods.

#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the object """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

if __name__ == "__main__":
    """ Test cases """
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()


# Solution Explained

# The Square class is defined, inheriting from the Rectangle class.

# The constructor (__init__) of the Square class calls the constructor of the Rectangle class,
#  using the super() function with the provided arguments size, size, x, y, and id.
#  This ensures that the behavior of Rectangle is maintained while creating a square with equal width and height.

# The __str__ method is overridden in the Square class to provide a customized string representation,
#  that includes the class name, ID, position, and size of the square.

# The provided test cases in the 9-main.py script create instances of the Square class,
#  and demonstrate various methods such as __str__, area, and display