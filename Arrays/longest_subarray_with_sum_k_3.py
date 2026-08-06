# This fucntion is to find the longest subarray whose sum is equal to target sum using 2 pointer approach
# Pseudo Code:
"""
arr = [1,2,3,1,1,1,1,4]
target = 3

longest_subarray(arr,target):
    i ,j =0
        for j in range(0,n):
            sum += arr[j]
            
            while sum > target:
                sum -=arr[left]
                left+=1
            
            if sum == target:
                maxlen = max(maxlen, j-i+1)
            
    return maxlen

"""


# Implementation: 

def longest_subarray(arr, target):
    n = len(arr)
    sum = 0
    left = 0
    max_len = 0

    for right in range(n):
        sum += arr[right]

        # check if sum > target:
        while sum > target:
            sum -=arr[left]
            left+=1

        # if sum = target:
        if sum == target:
            max_len = max(max_len,right-left+1)
    return max_len

arr = [1,2,3,1,1,1,1,4]
target = 4

result = longest_subarray(arr,target)
print(f"The length of the longest subarray that sums upto the given tagert:{target} is {result}")


# T.C = o(2n)
# S.C = o(1)