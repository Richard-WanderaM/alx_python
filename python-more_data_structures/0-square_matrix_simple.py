 # Create an empty matrix with the same dimensions as the input matrix

def square_matrix_simple(matrix=[]):
   
    new_matrix = [[0 for _ in row] for row in matrix]

    # Iterate through each element of the input matrix and compute the square value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix


# The new_matrix contains the square values of the elements in the input matrix,
# while the original matrix remains unchanged

#QUESTION 

# Write a function that computes the square value of all integers of a matrix.

# Prototype: def square_matrix_simple(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified
# You are not allowed to import any module
# You are allowed to use regular loops, map, etc.