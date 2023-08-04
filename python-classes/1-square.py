class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)  # Attempting to access private attribute directly raises an error
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)  # Attempting to access private attribute with name mangling raises an error
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")  # Attempting to initialize with a non-integer value raises an error
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)  # Attempting to initialize with a negative value raises an error
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)