# This function returns the majority elements from the given array, if the element is > n/3 times then it is majority element.

# Brute force:

# Pseudo code:
""" 
arr = [1,1,1,1,3,2,2,2]

use hashing, to store the count and check the condition on the go
"""

# Implementation:

def maj_ele(arr):
    ans = []
    hash_map = {}
    for ele in arr:
        hash_map[ele] = hash_map.get(ele,0)+1
        if hash_map[ele] == (len(arr)//3):
            ans.append(ele)
        
    print(f"majority elements in the array are:{ans}")
    return None

arr = [1,1,1,1,3,2,2,2]
maj_ele(arr)

# T.C = O(n)
# S.C = O(n)