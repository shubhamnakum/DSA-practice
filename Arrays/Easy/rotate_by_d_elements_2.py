# This function is to rotate each elements in an array by d element using optimal approach. 

# Psuedo Code : 
"""
arr = [1,2,3,4,5,6,7]

def rotate(arr,d):
    reverse(a,a+d)
    reverse(a+d,a+n)
    reverse(a,a+n)

"""

# Implementation : 

def rotate(arr,d):
    n = len(arr)
    d = d % n

    arr[0:d] = arr[0:d][::-1]  # reverse the first part
    arr[d:] = arr[d:][::-1] # reverse the second part
    arr.reverse()
    return arr

arr = [1,2,3,4,5,6,7]
d = 3
result = rotate(arr,d)
print(f"Rotated array: {result}")

# T.C = o(2n)
# S.C = o(1)