# This function is to find count of all occurance of a element in array using hashing


# Psuedo Code:
"""
arr 

count_occ(arr):
    hash_map = {}
    for each element in arr:
        hash_map[element] += 1
    return hash_map
"""

# Implementation:

def count_occ(arr):
    hash_map = [0] * len(arr)
    for i in range(0,len(arr)-1):
        element = arr[i]
        hash_map[element] += 1
    return hash_map


arr = [1,2,3,1,2,4,5,3,8,7,4]
hash_map = count_occ(arr)
query = int(input("Enter a number to find count of all it occurances: "))
print(f"count of element {query} in array  is {hash_map[query]}.")


# T.C = O(n)
# S.C = O(n)