a = 1
b = 2

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

if __name__ == "__main__":
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))

# Write a program that imports the function def add(a, b): 
# from the file add_0.py and prints the result of the addition 1 + 2 = 3

# You have to use print function with string format to display integers
# You have to assign:
# the value 1 to a variable called a
# the value 2 to a variable called b
# and use those two variables as arguments when calling the functions add and print
# a and b must be defined in 2 different lines: a = 1 and another b = 2
# Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
# You can only use the word add_0 once in your code
# You are not allowed to use * for importing or __import__
# Your code should not be executed when imported - by using __import__,