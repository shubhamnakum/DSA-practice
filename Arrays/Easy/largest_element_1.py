# This Function is to Find the largest element in the given array using Brute force.

# Psuedo Code:
"""
arr = [2,3,4,2,5,3,7,8,4]

largest_ele(arr):
    sort(arr)  // sort the array
    largest = arr[-1] // pick the last element
    return largest
"""

# Implementation: 


def find_large(arr):
    arr.sort()
    largest = arr[-1]
    return largest

arr = [2,3,4,2,5,3,7,8,4]
max = find_large(arr)
print(f"Largest element in the array is: {max}")


# T.C = o(nlogn) //due to sorting
# S.c = o(n)