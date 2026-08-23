# This Function is to find the max sum of the subarray using the better approach with 2 nested loops:

# Pseudo code:
"""
arr = [-2,-3,4,-1,-2,1,5,-3]

use nested loops i and j and sum directly while looping
check the sum is max or not
"""

# Implementation:

def max_sum(arr):
    max_sum = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            max_sum = max(max_sum, sum)
    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
result = max_sum(arr)
print(f"result : {result}")

# T.C = O(n^2)
# S.C = O(1)