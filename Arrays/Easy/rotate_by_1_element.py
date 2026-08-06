# This function is to rotate each elements in an array by 1 element. 

# Psuedo Code : 
"""
arr = [1,2,3,4,5,6,7]

def rotate(arr):
    temp = arr[0]
    for i =1, i<n : 
        arr[i-1] = arr[i]
    arr[n-1] = temp

"""

# Implementation : 

def rotate(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

arr = [1,2,3,4,5,6,7]
result = rotate(arr)
print(f"Rotated array: {result}")

# T.C = o(n)
# S.C = o(1)