# Find the value at given index R and C from the pascals triangle. 
# Brute force:
#Pseudo Code:
""" 
pascals_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
]

run a nested loop and generate value at each pos using ncr formula
"""

# Implementation:

def findnCr(n,r):
    ans = 1
    for i in range(0,r):
        ans = ans*(n-i)
        ans = ans//(i+1)
    return ans

def generateTriangle(row):
    ans = []
    for i in range(1,row+1):
        temp = []
        for j in range(1,i+1):
            temp.append(findnCr(i-1,j-1))
        ans.append(temp)
    print(ans)
    return None

pascals_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
]
generateTriangle(6)


# T.C = o(n*n*r) = o(n^3)
# S.C = o(1)