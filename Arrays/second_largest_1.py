# Find the second largest element in the array using brute force approach:

# Pseudo code:
"""
arr = [3,9,2,1,4,7,9,3]

find_sec_largest(arr):
    sort(arr)
    max = arr[-1]
    for i=n-2 --> 0:
        if (arr[i] != max):
            smax = arr[i]
            break
    return smax
"""

# Implementation:

def find_sec_largest(arr):
    arr.sort()
    max = arr[-1]
    n = len(arr)
    for i in range(n-2,-1,-1):
        if arr[i] != max:
            smax = arr[i]
            break
    return smax

arr = [3,9,2,1,4,7,10,10,3]
smax = find_sec_largest(arr)
print(f"Second largest element in the array is: {smax}")

# T.C = o(nlogn )   // best and average case
# T.C = o(nlogn + n) // worst case (i.e second largest is at 0th index)
# S.C = o(n)