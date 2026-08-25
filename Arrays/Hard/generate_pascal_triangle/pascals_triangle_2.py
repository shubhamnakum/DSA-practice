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

run a nested loop and generate row using type 2 solution
"""

# Implementation:


def generateRow(row):
    res = []
    ans=1
    res.append(ans)
    for i in range(1,row):
        ans = ans*(row-i)
        ans = ans//(i)
        res.append(ans)
    return res

def generateTriangle(row):
    ans = []
    for i in range(1,row+1):
        ans.append(generateRow(i))
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


# T.C = o(n*n) = o(n^2)
# S.C = o(1)