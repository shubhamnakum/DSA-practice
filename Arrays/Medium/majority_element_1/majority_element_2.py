# This function is to find the majority occuring element from the given array using hashing approach:

# Pseudo Code:
"""
arr = [2,2,3,3,1,2,2]

create a hashmap of (ele,cnt) and store the values
do a one pass again and find the majority element
"""

# Implementation:

def majority(arr):
    hash = {}
    for i in range(len(arr)):
        if arr[i] in hash:
            hash[arr[i]] += 1
        else: 
            hash[arr[i]] = 1
    for i in range(len(hash)):
        if hash[arr[i]] > len(arr)//2 :
            return arr[i]
    return -1

arr = [2,2,3,3,1,2,2]
result = majority(arr)
print(f"Result : {result}")

# T.C = o(2n)
# S.C = o(n)