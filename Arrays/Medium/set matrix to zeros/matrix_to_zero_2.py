# Given the matrix of 0/1 convert those rows and column to 0 where initially 0 existed.

# Bruteforce :
""" 
matrix = [[1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]


iterate each element of the matrix, and see if the element is 0, mark it to 1 in external array
then reitreate and see if either of markers(row or col) are 0 then convert the element to 0.
"""

# Implementation: 

def matrix_to_zero(mat):
    n = len(mat)  # column size
    m = len(mat[0]) # row size
    
    row_mark = [0]*m
    col_mark = [0]*n
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                row_mark[j] = 1
                col_mark[i] = 1
    
    for i in range(n):
        for j in range(m):
            if row_mark[j] == 1 or col_mark[i] == 1:
                mat[i][j] = 0
    
    print(f"matrix :\n {mat}")
    return None

matrix = [[1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]
matrix_to_zero(matrix)

# T.C = o(n*m) +o(n*m) = o(n^2)
# S.C = o(n+m)