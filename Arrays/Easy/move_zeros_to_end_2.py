# This Function is to move all zeros to end using 2 pointer approach:

# Pseudo code:
"""
arr = [1,2,4,0,0,5,1,0,1]

move_zeros(arr):
    1. find 1st 0th index
    2. swap that with next non-zero element
    3. keep on repeating it
"""


def swap(a,b):
    a,b =b,a
    return a,b
def move_zeros(arr):
    j = -1
    n =len(arr)
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1,n):
        if (arr[i] != 0):
            arr[j],arr[i] = swap(arr[j],arr[i])
            j+=1
    return arr


arr = [1,2,4,0,0,5,1,0,1]
result = move_zeros(arr)
print(f"resultant array is : {result}")

# T.C = O(n)
# S.C = o(1)