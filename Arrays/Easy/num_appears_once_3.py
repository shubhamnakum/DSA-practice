# This function is to find the number that appears once and others twices in the array using XOR approach:

# Pseudo code:
"""
a = [1,1,2,3,3,4,4]

once_occured(a):
    iterate over the array and perform the XOR operation
"""


# Implementation:
def once_occured(arr):
    xor = 0

    for num in arr:
        xor = xor ^ num

    return xor


arr = [1,1,2,3,3,4,4]
result = once_occured(arr)
print(f"the number that only occured once is : {result}")

# T.C = o(n)
# S.C = O(1)