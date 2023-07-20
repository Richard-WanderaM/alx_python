def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_list = [0, 1]
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    return fib_list[:n]

# Write a Python function called fibonacci_sequence
# that takes a number n as input and returns a list of the first n Fibonacci numbers.

# Prototype: def fibonacci_sequence(n)
# Returns a list of the first n Fibonacci numbers.
# You are not allowed to import any module.
# Return an empty list if the it is not possible to generate the Fibonacci numbers for n
# You don’t need to understand __import__