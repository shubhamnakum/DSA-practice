# This Function is to Find the largest element in the given array using optimal approach.

# Psuedo Code:
"""
arr = [2,3,4,2,5,3,7,8,4]

find_large(arr):
    max = 0
    for i=0-->n-1:
        if (arr[i]>max):
            max = arr[i]
    return max
    
"""

# Implementation: 


def find_large(arr):
    max = 0
    for i in arr:
        if arr[i] > max: 
            max = arr[i]
    return max

arr = [2,3,4,2,5,3,7,8,9,4]
max = find_large(arr)
print(f"Largest element in the array is: {max}")


# T.C = o(n) 
# S.c = o(1)