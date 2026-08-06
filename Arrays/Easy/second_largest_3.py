# Find the second largest element in the array using a better approach 

# Psuedo Code: 
"""
arr = [3,9,2,1,4,7,9,3]

find_sec_largest(arr):
    max = 0 , smax = -1  //if all numbers are >0

    for i=0 --> n-1:
        if (arr[i]>max):
            smax = max
            max = arr[i]
        elif (arr[i]<max and arr[i]>smax):
            smax = arr[i]
    return smax
"""

# Implementation:

def find_sec_largest(arr):
    max = 0
    smax = -1

    for num in arr:
        if num > max:
            smax = max
            max = num
        elif (num < max and num > smax):
            smax = num
    return smax

arr = [3,9,2,1,4,7,10,10,3]
smax = find_sec_largest(arr)
print(f"Second largest element in the array is: {smax}")

# T.C = o(n)
# S.C = o(1)