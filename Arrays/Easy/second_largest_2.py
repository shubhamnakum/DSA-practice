# Find the second largest element in the array using a better approach 

# Psuedo Code: 
"""
arr = [3,9,2,1,4,7,9,3]

find_sec_largest(arr):
    max = 0 , smax = -1  //if all numbers are >0

    // first pass to find max element
    for i = 0 to n-1:
        if (arr[i] > max):
            max = arr[i]
    
    // Second pass to find sec largest element
    for i = 0 to n-1:
        if (arr[i] > smax && arr[i]!=max):
            smax = arr[i]
    return smax
"""

# Implementation:

def find_sec_largest(arr):
    max = 0
    smax = -1

    # first pass to find largest element
    for num in arr:
        if num > max :
            max = num

    # second pass to find second largest element
    for num in arr:
        if (num >smax and num !=max):
            smax = num
    return smax

arr = [3,9,2,1,4,7,10,10,3]
smax = find_sec_largest(arr)
print(f"Second largest element in the array is: {smax}")

# T.C = o(2n)
# S.C = o(1)