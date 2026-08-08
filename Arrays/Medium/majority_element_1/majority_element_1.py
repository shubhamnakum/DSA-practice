# This function is to find the majority occuring element from the given array using bruteforce approach:

# Pseudo Code:
"""
arr = [2,2,3,3,1,2,2]

for i=0-->n:
    for j=0-->n:
        if arr[j] = arr[i]:
            cnt+=1
    if cnt > n//2:
        return arr[i]
"""

# Implementation:

def majority(arr):
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[j] == arr[i]:
                cnt+=1
        if cnt > len(arr) // 2 :
            return arr[i]
    return -1

arr = [2,2,3,3,1,2,2,3,3,3,3,3]
result = majority(arr)
print(f"Result : {result}")

# T.C = o(n^2)
# S.C = o(1)