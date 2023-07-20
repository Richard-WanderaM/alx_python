def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Write a Python function called is_prime 
# that takes a number as input and returns True 
# if the number is prime, and False otherwise.

# Prototype: def is_prime(number)
# Returns True if the number is prime, and False otherwise.
# You are not allowed to import any module.
# You don’t need to understand __import__