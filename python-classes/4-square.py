class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)

# Test the Square class
if __name__ == "__main__":
    try:
        # Test valid input
        square1 = Square(5)
        square1.my_print()
        print("Area:", square1.area())

        # Test invalid input
        square2 = Square("invalid")  # This should raise a TypeError
    except Exception as e:
        print("Error:", e)
