# Given the matrix of 0/1 convert those rows and column to 0 where initially 0 existed.

# Bruteforce :
""" 
matrix = [[1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]


iterate each element of the matrix, and see if the element is 0, if so then mark that elements row and column to -1
then again iterate the matrix and convert -1 to 0
"""

# Implementation: 

def matrix_to_zero(mat):
    n = len(mat)  # column size
    m = len(mat[0]) # row size
    
    
    def mark_rows(i):
        for j in range(m):
            if mat[i][j] != 0:
                mat[i][j] = -1
    
    def mark_cols(j):
        for i  in range(n):
            if mat[i][j] != 0:
                mat[i][j] = -1
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                mark_rows(i)
                mark_cols(j)
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == -1:
                mat[i][j] = 0
    
    print(f"matrix :\n {mat}")
    return None

matrix = [[1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]
matrix_to_zero(matrix)

# T.C = o(n*m)*o(n+m) +o(n*m) = o(n^3)
# S.C = o(1)