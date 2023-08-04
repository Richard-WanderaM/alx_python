class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size (side length) of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size (side length) of the square.
        """
        self.__size = size

# Test code
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)  # Will raise an AttributeError
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)  # Will raise an AttributeError
    except Exception as e:
        print(e)
