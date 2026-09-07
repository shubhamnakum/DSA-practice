# Find the total subarray whose XoR is target K.

# Better Approach:

# Psuedo code: 
"""
a = [4,2,2,6,4]

run through each subarray and then instead of iterating each individual elements in subarray and XOR it.
only the xor the new element with previous xor
check if it mactches k
"""

# Implementation:

def sa_xor_count(arr,k):
    cnt = 0 
    n = len(arr)
    for i in range(n):
        xor = 0
        for j  in range(i,n):
            xor = xor ^ arr[j]
            if xor == k:
                cnt+=1
    
    print(f"total subarrays whose xor matches k is: {cnt}")
    return None

a = [4,2,2,6,4]
k=6
sa_xor_count(a,k)


# T.C = O(n^2)
# S.C = O(1)