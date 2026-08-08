# This Function is to find the max sum of the subarray using the Kadane's algorithm:

# Pseudo code:
"""
arr = [-2,-3,4,-1,-2,1,5,-3]


1. Take a pointer and iterate over the array
2. Take 2 var max_sum & sum
3. if sum < 0 then reset it else keep on adding and update the max_sum
"""

# Implementation:

def max_sum(arr):
    max_sum = 0
    sum = float('-inf')
    best_start = 0 
    best_end = 0

    for i in range(len(arr)):
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            best_start = start
            best_end = i
        if sum < 0 :
            sum = 0
    return max_sum, best_start, best_end

arr = [-2,-3,4,-1,-2,1,5,-3]
result,start,end = max_sum(arr)
print(f"result : {result} and starts : {start} and ends : {end}")

# T.C = O(n)
# S.C = O(1)