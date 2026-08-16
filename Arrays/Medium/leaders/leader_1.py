# Find the elements that are leaders,(Leaders are those element if its greater than all elements in right)
# Nested loop

# Pseudo Code:
"""
arr = [3,8,2,5,1,3,3]

run a nested loop and check if the elements on right is smaller or not
"""

# Implementation:

def leaders(arr):
    result = []
    for i in range(len(arr)):
        leader = True
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                leader = False
                break
        if leader == True:
            result.append(arr[i])
    return result

arr = [3,8,2,5,1,3,3]
result = leaders(arr)
print(f"leaders in the array are : {result}")

# T.C = o(n^2)
# S.C = o(n) // for returning the array