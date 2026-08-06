# This function is to find the missing element in a given array from 1 to N using XOR.


# Pseudo code:
"""
arr = [1,2,4,5]

find_missing_element(arr):
    n = len(arr)+1
    xor_1 = 0
    xor_2 = 0

    for i = 0 --> n-1:
        xor_2 = xor_2 ^ arr[i]
        xor_1 = xor_1 ^ (i+1)
    xor_1 = xor_1 ^ n
    return xor_1 ^ xor_2
"""

def missing_element(arr):
    n = len(arr)+1
    xor_1 = 0
    xor_2 = 0

    for i in range(0,n-1):
        xor_2 = xor_2 ^ arr[i]
        xor_1 = xor_1 ^ (i+1)
    xor_1 = xor_1 ^ n
    return xor_1 ^ xor_2

arr = [1,2,3,5]
missing_elem = missing_element(arr)
print(f"missing element in array is : {missing_elem}")


# T.C = o(n)
# S.C = o(1)