# Rotate Matrix by 90 degree clockwise using the optimal approach:

# Pseudo Code:
"""
matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

1. Transpose the matrix
2. reverse each row
"""

# Implementation

def rotate_matrix(mat):
    n = len(mat)
    for i in range(n-1):
        for j in range (1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
    return mat

matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

result = rotate_matrix(matrix)
print(f"roateted matrix : {result}")


# T.C = O(n^2)
# S.C = o(1)