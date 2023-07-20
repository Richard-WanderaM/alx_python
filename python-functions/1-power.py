def pow(a, b):
    if b == 0:
        return 1

    result = 1
    reciprocal = False

    if b < 0:
        reciprocal = True
        b = abs(b)

    for _ in range(b):
        result *= a

    return 1 / result if reciprocal else result

# Write a function that computes a to the power of b and return the value.

# Prototype: def pow(a, b):
# Returns the value of a ^ b
# You are not allowed to import any module
# You don’t need to understand __import__