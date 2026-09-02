# given an array, find the quadralets that sums upto target using bruteforce approach.

# Pseudo Code:
""" 
arr = [-1,0,1,2,-1,-4]

using naive nested loop approach
"""

# Implementation: 

def sum_4(arr,target):
    temp_ans = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[l] == target:
                        temp_list = [arr[i],arr[j],arr[k],arr[l]]
                        temp_list.sort()
                        temp_ans.add(tuple(temp_list))
    
    ans = list(temp_ans)
    print(f"all triplets are: {ans}")
    return None

arr = [-1,0,1,2,-1,-4]
target = 1
sum_4(arr,target)

# T.C = O(n^4)
# S.C = O(no. of quads)