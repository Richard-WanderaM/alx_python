def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end=" " if i < len(row) - 1 else "")
        print()


# for row in matrix:: This loops over each row in the input matrix.

# for i in range(len(row)):: This loops over each element (integer) in the current row.

# print("{:d}".format(row[i]), end=" " if i < len(row) - 1 else ""): This prints the current integer using string formatting with "{:d}". The end parameter is used to customize the separator between integers in the same row. If we are not at the last element of the row (i < len(row) - 1), we print a space after the integer; otherwise, we don't add any separator to the end of the line.

# print(): After printing all integers in a row, we add a new line to move to the next row.