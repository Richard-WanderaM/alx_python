class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)  # Attempting to access private attribute directly raises an error
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)  # Attempting to access private attribute with name mangling raises an error
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
