# given an array, find the quadralets that sums upto target using hashing approach

# Pseudo Code:
""" 
arr = [-1,0,1,2,-1,-4]

using nested loops but with hashing
if we have 4 elements then 4th element will always be l = -(i+j+k)
so we search if l exists in hash or not.
"""

# Implementation: 

def sum_4(arr, target):
    temp_ans = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            hash = set()
            for k in range(j+1,n):
                fourth = target - (arr[i] + arr[j] + arr[k])
                if fourth in hash:
                    temp_list = [arr[i], arr[j], arr[k], fourth]
                    temp_list.sort()
                    temp_ans.add(tuple(temp_list))
                hash.add(arr[k])
    
    ans = list(temp_ans)
    print(f"all triplets are: {ans}")
    return None

arr = [-1,0,1,2,-1,-4]
target = 1
sum_4(arr, target)

# T.C = O(n^3)
# S.C = O(no. of qauds) + o(n)