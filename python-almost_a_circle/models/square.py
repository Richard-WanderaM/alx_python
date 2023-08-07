#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of the object """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

if __name__ == "__main__":
    """ Test cases """
    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))


# Question

# Update the class Square by adding the public getter and setter size

# The setter should assign (in this order) the width and the height - with the same value

# The setter should have the same value validation as the Rectangle for width and height
#  - No need to change the exception error message (It should be the one from width)



# Final Solution Explanation

# The size property is added as a getter for the size attribute.
#  It returns the width of the square.

# The size setter is added to update both the width and height attributes with the same value.
#  The same validation as in the Rectangle class is used for the width attribute.

# The provided test cases in the 10-main.py script create an instance of the updated Square class,
#  and demonstrate the getter and setter for the size attribute.