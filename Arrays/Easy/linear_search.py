# This function is to search a element in the array :

# Pseudo code:
"""
arr = [6,7,8,2,3,5,1]

for i in arr : 
    if i exist then return the index
retrun -1
"""

# Implementation:

def linear_search(arr,num):
    for i in range(0,len(arr)):
        if arr[i]==num:
            return i
    return -1

arr = [6,7,8,2,3,5,1]
num = 5
result = linear_search(arr,num)
print(f"number {num} is at {result}th position in the array.")


# T.C = o(n)
# S.C = o(1)