# This is function to identify if the array is sorted or not:

# Psuedo Code:
"""
arr = [2,3,4,5,6,7]
is_sorted(arr):
    for i = 0 --> n-1:
        if arr[i] < arr[i+1]:
        else:
            return false
    return true
"""

# Implementation:

def is_sorted(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i] < arr[i+1]:
            None
        else: 
            return False
    return True

arr = [2,3,4,3,6,7]
res = is_sorted(arr)
print(f"is the current array sorted : {res}")


# T.C = o(n)
# S.C = o(1)