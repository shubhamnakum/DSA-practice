# Rearrange elements of array with equal positive and negative elements in alternate manner using bruteforce.

# Psuedo Code:
"""
arr = [3,1,-2,-5,2,-4]

iterate and split the array into 2 arrays pos and neg
then append from both in the original array
"""

# Implementation

def rearrange(arr):
    n = len(arr)
    pos = []
    neg = []
    for ele in arr:
        if ele > 0:
            pos.append(ele)
        else: 
            neg.append(ele)
    for i in range(n//2):
        arr[2*i] = pos[i]
        arr[2*i + 1] = neg[i]

    print("rearrabged array :",arr)
    return None

arr = [3,1,-2,-5,2,-4]
rearrange(arr)

# T.C = o(n)
# S.C = O(n)