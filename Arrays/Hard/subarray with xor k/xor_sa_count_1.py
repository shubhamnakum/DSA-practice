# Find the total subarray whose XoR is target K.

# Brute force:

# Psuedo code: 
"""
a = [4,2,2,6,4]

run through each subarray and then iterate each individually elements in subarray and XOR it.
check if it mactches k
"""

# Implementation:

def sa_xor_count(arr,k):
    cnt = 0 
    n = len(arr)
    for i in range(n):
        for j  in range(i,n):
            xor = 0
            for index in range(i,j+1):
                xor = xor ^ arr[index]
            if xor == k:
                cnt+=1
    
    print(f"total subarrays whose xor matches k is: {cnt}")
    return None

a = [4,2,2,6,4]
k=6
sa_xor_count(a,k)


# T.C = O(n^3)
# S.C = O(1)