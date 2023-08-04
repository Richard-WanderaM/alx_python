class Square:
    def __init__(self, size):
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)  # Attempting to access private attribute directly raises an error
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)  # Attempting to access private attribute with name mangling raises an error
    except Exception as e:
        print(e)
