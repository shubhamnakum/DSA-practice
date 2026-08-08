# This function is to find the majority occuring element from the given array using Boyer-Moores voting approach:

# Pseudo Code:
"""
arr = [2,2,3,3,1,2,2]

voting algo:
1. Take a element as candidate
2. Increment if the current element is candidate else decrement the count untill it reaches 0.
3. if the count doesnt reaches till array end, then that number is candidate majority element.
4. if the PS doesnt clarify about the majority element will surely exists then check the cand maj ele > n/2.
"""

# Implementation:

def majority(arr):
    cand = 0
    cnt = 0
    cand_cnt = 0
    for i in range(len(arr)):
        if cnt == 0:
           cand = arr[i]
           cnt = 1
        elif arr[i] == cand:
           cnt+=1
        else: 
           cnt-=1
    for i in range(len(arr)):
       if arr[i] == cand:
          cand_cnt+=1
    if cand_cnt > len(arr)//2:
       return cand
    return -1

arr = [2,2,3,3,1,2,3,3,3]
result = majority(arr)
print(f"Result : {result}")

# T.C = o(2n)
# S.C = o(1)