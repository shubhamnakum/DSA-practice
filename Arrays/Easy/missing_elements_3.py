# This function is to find the missing element in a given array from 1 to N using summation.


# Pseudo code:
"""
arr = [1,2,4,5]

find_missing_element(arr):
    n = len(arr)+1
    sum_1 = n(n+1) / 2
    sum_2 = 0

    for (i=0 --> n):
        sum_2 = sum_2 + arr[i]
    return sum_1 - sum_2
"""

def missing_element(arr):
    n = len(arr)+1
    sum_1 = (n*(n+1)) // 2
    sum_2 = 0

    for i in range(0,n-1):
        sum_2 = sum_2 + arr[i]
    return sum_1 - sum_2

arr = [1,2,4,5]
missing_elem = missing_element(arr)
print(f"missing element in array is : {missing_elem}")


# T.C = o(n)
# S.C = o(1)