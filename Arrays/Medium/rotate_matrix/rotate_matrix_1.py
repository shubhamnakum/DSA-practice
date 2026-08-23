# Rotate Matrix by 90 degree clockwise using the bruteforce approach:

# Pseudo Code:
"""
matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

run a nested loop and place the ith element to n-1-i the place.
"""

# Implementation

def rotate_matrix(mat):
    n = len(matrix)
    ans = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans[j][n-1-i]=matrix[i][j]
    return ans

matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

result = rotate_matrix(matrix)
print(f"roateted matrix : {result}")


# T.C = O(n^2)
# S.C = o(n^2)