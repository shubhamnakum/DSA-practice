# Find the elements that are leaders,(Leaders are those element if its greater than all elements in right)
# 

# Pseudo Code:
"""
arr = [3,8,2,5,1,3,3]

run a one pass from R-->L, update the max so far by checking if current > max
"""

# Implementation:

def leaders(arr):
    result = []
    max = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > max:
            max = arr[i]
            result.append(arr[i])
    return result

arr = [3,8,2,5,1,3,3]
result = leaders(arr)
print(f"leaders in the array are : {result}")

# T.C = o(n)
# S.C = o(n) // for returning the array