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

