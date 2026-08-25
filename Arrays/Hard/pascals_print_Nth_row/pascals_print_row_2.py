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
so run a loop and genrate values using ans*(row-col)/col formula.
"""

# Implementation:



def generateRow(row):
    ans = 1
    print(ans)
    for i in range(1,row+1):
        ans = ans*(row-i)
        ans = ans//(i)
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
generateRow(6)


# T.C = o(n)
# S.C = o(1)