# Given a matrix, traverse it and print all the elements in the spiral fashion

# Pseudo Code:
""""
matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
    
initialize the top,bot,left,right
run a while loop and print right array, print bottom array, print left array, print top array.
"""

# Implementation: 

def spiral(mat):
    ans = []
    n = len(mat)
    m = len(mat[0])
    left = 0 
    right = m-1
    top = 0
    bottom = n-1

    while (top<=bottom and left <= right):
        for i in range(left,right+1):
            ans.append(mat[top][i])
        top+=1
        for i in range(top,bottom+1):
            ans.append(mat[i][right])
        right-=1
        if (top<=bottom):
            for i in range(right, left-1,-1):
                ans.append(mat[bottom][i])
            bottom-=1
        if (left<=right):
            for i in range(bottom,top-1,-1):
                ans.append(mat[i][left])
            left+=1
            
    
    print(ans)
    return None

matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
spiral(matrix)


# T.C = O(n*m)
# S.C = O(n*m)