# This function is to find the number that appears once and others twices in the array using bruteforce approach:

# Pseudo code:
"""
a = [1,1,2,3,3,4,4]

once_occured(a):
    take a number, do a linear search across the array
    if the num exists again then increment the counter
    if counter remains 1 then return the num
"""


# Implementation:
def once_occured(arr):
    
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[j] == arr[i]:
                cnt+=1
        if cnt == 1:
            return arr[i]

arr = [1,1,2,3,3,4,4]
result = once_occured(arr)
print(f"the number that only occured once is : {result}")

# T.C = o(n^2)
# S.C = O(1)