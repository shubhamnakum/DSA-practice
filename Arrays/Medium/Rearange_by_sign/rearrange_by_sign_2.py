# Rearrange elements of array with equal positive and negative elements in alternate manner using single pass.

# Psuedo Code:
"""
arr = [3,1,-2,-5,2,-4]

create 2 var pos and neg with 0,1. 
based on sign of element append it in the array and update the vars.
"""

# Implementation

def rearrange(arr):
    n = len(arr)

    result = [0] * n

    pos_ind = 0
    neg_ind = 1

    for ele in arr:
        if ele < 0:
            result[neg_ind] = ele
            neg_ind += 2
        else:
            result[pos_ind] = ele
            pos_ind += 2

    print("rearranged array:", result)
    return result

arr = [3,1,-2,-5,2,-4]
rearrange(arr)

# T.C = o(n)
# S.C = O(n) 