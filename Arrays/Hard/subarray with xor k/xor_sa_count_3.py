# Find the total subarray whose XoR is target K.

# optimal Approach (hashing + prefix sum):

# Psuedo code: 
"""
a = [4,2,2,6,4]

we use the prefix sum idea here and see if the required is there or not in hash.

req = curr_xor ^ K

if req in hash:
    cnt += hash[req]
hash[curr_xor] = hash.get(curr_xor,0) + 1
"""

# Implementation:

def sa_xor_count(arr,k):
    cnt = 0 
    hash = {}
    hash[0] =1
    curr_xor = 0
    for num in arr:
        curr_xor = curr_xor ^ num
        req = curr_xor ^ k
        
        if req in hash:
            cnt += hash[req]
        hash[curr_xor] = hash.get(curr_xor,0)+1
    
    print(f"total subarrays whose xor matches k is: {cnt}")
    return None

a = [4,2,2,6,4]
k=6
sa_xor_count(a,k)


# T.C = O(n)
# S.C = O(n)