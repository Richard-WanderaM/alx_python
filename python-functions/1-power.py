def pow(a, b):
    result = 1.0
    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result /= a
    return result
