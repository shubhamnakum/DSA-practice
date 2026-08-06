# This Function is to remove duplicate elements from the sorted array, in-place.
# 2 pointer Approach


# Psuedo Code:
"""
arr = [1,1,2,2,2,3,3,4]

remove_dups(arr):
    i = 0 
    for (j=1 to n):
        if (arr[j]!= arr[i]):
            arr[i+1] = a[j]
            i++
    return arr

"""

# Implementation:

def remove_dups(arr):
    i=0
    for j in range(1,len(arr)):
        if (arr[j] != arr[i]):
            arr[i+1] = arr[j]
            i+=1
    return arr[0:i+1]


arr = [1,1,2,2,2,3,3,4,4,4,6,6,9,8,8]
unique_arr = remove_dups(arr)
print(f"Unique elements in the array are :{unique_arr}")


# T.C = o(n)
# S.c = o(1)