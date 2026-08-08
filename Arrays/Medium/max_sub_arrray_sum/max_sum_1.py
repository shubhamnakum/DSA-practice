# This Function is to find the max sum of the subarray using the bruteforce approach:

# Pseudo code:
"""
arr = [-2,-3,4,-1,-2,1,5,-3]

use nested loops i and j
use another loop k and sum all elements from i to j
check the sum is max or not
"""

# Implementation:

def max_sum(arr):
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range(i,j):
                sum += arr[k]
            max_sum = max(max_sum, sum)
    return max_sum

arr = [-2,-3,4,-1,-2,1,5,-3]
result = max_sum(arr)
print(f"result : {result}")

# T.C = O(n^3)
# S.C = O(1)