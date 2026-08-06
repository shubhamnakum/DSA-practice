# This function is to rotate each elements in an array by d element using brute force.

# Psuedo Code : 
"""
arr = [1,2,3,4,5,6,7]

def rotate(arr,d):
    temp = arr[0:d]
    for i = d, i<n : 
        arr[i-d] = arr[i]
    
    for i = n-d, i<n:
        arr[i] = temp[i-(n-d)]

"""

# Implementation : 

def rotate(arr,d):
    n = len(arr)
    d = d % n

    temp = arr[0:d]
    
    for i in range(d,n):
        arr[i-d] = arr[i]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]
    return arr

arr = [1,2,3,4,5,6,7]
d = 15
result = rotate(arr,d)
print(f"Rotated array: {result}")

# T.C = o(n+d)
# S.C = o(d)