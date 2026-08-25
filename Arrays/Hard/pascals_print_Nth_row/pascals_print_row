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

we know that rth row will have r elements.
so run a loop and genrate values using ncr formula.
"""

# Implementation:

def findnCr(n,r):
    ans = 1
    for i in range(0,r):
        ans = ans*(n-i)
        ans = ans//(i+1)
    return ans

def generateRow(row):
    for i in range(1,row+1):
        print(findnCr(row-1,i-1))
    return None

pascals_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
]
generateRow(6)


# T.C = o(n*r)
# S.C = o(1)