# This Function is to find union of two arrays using brute force apporach:

# Psuedo code:
"""
a1= [1,1,2,3,4]
a2 = [2,3,4,4,5,6]

union(a1,a2):
    1. add all unique elements from arr1 into a new array
    2. add all unique elements from arr2 into the same new array

"""

# Implementation:

def union(a1,a2):
    union_arr = []
    # 1. add all unique elements of arr1 
    for ele in a1:
        if ele not in union_arr:
            union_arr.append(ele)

    # 2. add all unique elements of arr2
    for ele in a2:
        if ele not in union_arr:
            union_arr.append(ele)

    return union_arr

a1 = [1,1,2,3,4]
a2 = [2,3,4,4,5,6,6,7,9]
result = union(a1,a2)
print(f"union of two array is: {result}")

# T.C = o(n1^2 + n2^2)
# S.C = o(n1+n2)