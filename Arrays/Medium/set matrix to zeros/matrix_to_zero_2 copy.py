# Given the matrix of 0/1 convert those rows and column to 0 where initially 0 existed.

# Bruteforce :
""" 
matrix = [[1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]


iterate each element of the matrix, and see if the element is 0, mark it to 0 instead of using external array
then reitreate and see if either of markers(row or col) are 0 then convert the element to 0.
"""

# Implementation: 

def matrix_to_zero(mat):
    n = len(mat)  # column size
    m = len(mat[0]) # row size
    
    col0 = 1
    
    for i in range(n):
        if mat[i][0] == 0:   # if 1st col conatins any zero then convert the col0 to 0
            col0 = 0
            
        for j in range(1,m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
    
    # using those markers, idnetify and convert elements to 0
    
    for i in range(1,n):
        for j in range(1,m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    
    # handle the 1st row:
    # handle inner matrix
    if mat[0][0] == 0:
        for j in range(m):
            mat[0][j] = 0
    # handle 1st col:
    if col0 == 0:
        for i in range(n):
            mat[i][0] = 0
    
    print(f"matrix :\n {mat}")
    return None

matrix = [[1, 1, 0, 1], 
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0]]
matrix_to_zero(matrix)

# T.C = o(n*m) + o(n*m) = o(n*m)
# S.C = o(1)