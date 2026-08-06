# This function is to find the missing element in a given array from 1 to N using hashing.


# Pseudo code:
"""
arr = [1,2,4,5]

find_missing_element(arr):
    n = len(arr)+1
    hash = [0]*n+1
    for i in range(0,n+1):
        hash[arr[i]] = 1
    for i in range(1,n+1):
        if hash[i] == 0:
            return i

"""

def missing_element(arr):
    n = len(arr)+1
    hash = [0]*(n+1)
    for i in arr:
        hash[i] = 1
    for i in range(1,n+1):
        if hash[i] == 0:
            return i

arr = [1,2,4,5]
missing_elem = missing_element(arr)
print(f"missing element in array is : {missing_elem}")


# T.C = o(2n)
# S.C = o(n)