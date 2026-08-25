# Find the value at given index R and C from the pascals triangle. 

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

to find a element we can use the forumla : 
(R-1)
    C
    (C-1)

and we dont need to extend the nCr till 1 instead we can n till r.
"""

# Implementation:

def findnCr(n,r):
    ans = 1
    for i in range(0,r):
        ans = ans*(n-i)
        ans = ans/(i+1)
    print(f"value at R={n+1} and C={r+1} is {ans}")
    return None

pascals_triangle = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
]
findnCr(6-1,2-1)


# T.C = o(r)
# S.C = o(1)