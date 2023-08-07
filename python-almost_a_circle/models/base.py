#!/usr/bin/python3
""" Base module """

class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

if __name__ == "__main__":
    """ Test cases """
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)


# Question

# Write the first class Base:

# Create a folder named models with an empty file __init__.py inside - with this file,
#  the folder will become a Python package

# Create a file named models/base.py:

# Class Base:
# private class attribute __nb_objects = 0
# class constructor: def __init__(self, id=None)::
# if id is not None, assign the public instance attribute id with this argument value
#  - you can assume id is an integer and you don’t need to test the type of it
# otherwise, increment __nb_objects and assign the new value to the public instance attribute id
# This class will be the “base” of all other classes in this project. 
# The goal of it is to manage id attribute in all your future classes,
#  and to avoid duplicating the same code (by extension, same bugs)

# Explanation of my code :

# The Base class is defined, and a private class attribute __nb_objects is initialized to 0.
#  This attribute will be used to manage the ID values.

# The constructor method __init__ is defined.
# It takes an optional parameter id, which, if provided, sets the instance's id attribute to the given value.
# If id is not provided, it increments __nb_objects and assigns the new value to the instance's id attribute.

# The if __name__ == "__main__": block contains test cases to demonstrate the behavior of the Base class.