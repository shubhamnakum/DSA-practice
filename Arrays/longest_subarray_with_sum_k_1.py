# This fucntion is to find the longest subarray whose sum is equal to target sum using bruteforce approach

# Pseudo Code:
"""
arr = [1,2,3,1,1,1,1,4]
target = 3

longest_subarray(arr,target):
    for i = 0 --> n:
        for j = i --> n:
            sum = sum + arr[j]
        if sum == target:
            len = max(len, j-i+1)
    return len

"""


# Implementation: 

def longest_subarray(arr, target):
    n = len(arr)
    
    sa_len = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == target and j-i+1 > sa_len:
                a,b = i,j
                sa_len = j-i+1
    return sa_len,a,b

arr = [1,2,3,1,1,1,1,4]
target = 3

result,a,b = longest_subarray(arr,target)
print(f"The length of the longest subarray that sums upto the given tagert:{target} is {result} and indices are {a} to {b}")


# T.C = o(n^2)
# S.C = o(1)