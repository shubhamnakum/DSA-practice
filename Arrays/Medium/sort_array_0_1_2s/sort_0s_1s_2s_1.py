# This function is to sort the given array which contains only 0s,1s and 2s using bruteforce approach:


# Pseudo Code:
"""
arr = [0,1,2,0,1,2,1,2,0,0,0,1]

use any sort algorithm
"""

# Implementation : 

def sort_array(arr):
    arr.sort()
    return arr

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
result = sort_array(arr)
print(f"result of the unsorted array is : {result}")

# T.C = O(nlogn)
# S.C = O(n)