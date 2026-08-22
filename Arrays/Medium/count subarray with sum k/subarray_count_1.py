# find the total no. of subarrays with sum = k from the given array : 
# Bruteforce:

# Pseudo Code:
"""
arr = [1,2,3,-3,1,1,1,4,2,-3]    

run a nested loop to form all subarrays
iterate each subarray with a another loop and increase the count if sums to k
"""


# Implementation:
def total_subarray(arr,k):
    cnt = 0
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum+=arr[k]
            if sum == k:
                cnt+=1
    print(f"Total Subarrays with sum k: {cnt}")
    return None

arr = [1,2,3,-3,1,1,1,4,2,-3]    
total_subarray(arr,3)

# T.C = O(n^3)
# S.C = o(1)