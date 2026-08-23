# find the total no. of subarrays with sum = k from the given array : 
# Prefix sum Approach:

# Pseudo Code:
"""
arr = [1,2,3,-3,1,1,1,4,2,-3]    

using prefix sum we can find out the count
"""


# Implementation:
def total_subarray(arr,k):
    dict = {}
    dict[0] = 1
    n = len(arr)
    presum = 0
    cnt = 0
    for i in range(n):
        presum+=arr[i]
        residual = presum - k
        cnt = cnt + dict.get(residual,0)
        dict[presum]  = dict.get(presum,0) + 1
    print(f"Total Subarrays with sum k: {cnt}")
    return None

arr = [1,2,3,-3,1,1,1,4,2,-3]    
total_subarray(arr,3)

# T.C = O(n)
# S.C = o(n)