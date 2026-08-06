# This fucntion is to find the longest subarray whose sum is equal to target sum using hashing approach
# This method works for both postivies and negatives
# Pseudo Code:
"""
arr = [1,2,3,1,1,1,1,4]
target = 3

longest_subarray(arr,target):
    for i =0 --> n:
        // if the entire array from 0 to i sums to target
        if sum = target: 
            max_len = i+1
        
        // check if the exists a prefix sum :
        rem = sum - target
        if rem in prefix_map: 
            length = i - prefix_map[rem]
            max_len = max(max_len, length)
        
        // store only the 1st occurence :
        if sum not in prefix_map:
            prefix_map[sum] = i
    return len

"""


# Implementation: 

def longest_subarray(arr, target):
    n = len(arr)
    prefix_map = {}
    sum = 0
    max_len = 0
    for i in range(n):
        sum += arr[i]
        # check if the sum from 0 to i is target:
        if sum == target:
            max_len = i+1

        # check if there exists a prefix sum in the hash map:
        rem = sum - target
        if rem in prefix_map:
            length = i - prefix_map[rem]
            max_len = max(max_len,length)

        # only store the 1st occurence :
        if sum not in prefix_map:
            prefix_map[sum] = i
    return max_len

arr = [1,2,3,1,1,1,1,4]
target = 4

result = longest_subarray(arr,target)
print(f"The length of the longest subarray that sums upto the given tagert:{target} is {result}")


# T.C = o(n)
# S.C = o(n)