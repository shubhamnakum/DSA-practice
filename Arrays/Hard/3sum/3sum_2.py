# given an array, find the triplets that sums upto 0 using better approach

# Pseudo Code:
""" 
arr = [-1,0,1,2,-1,-4]

using nested loops but with hashing
if we have 2 elements then 3rd element will always be r = -(p+q)
so we search if r exists in hash or not.
"""

# Implementation: 

def sum_3(arr):
    temp_trip = set()
    n = len(arr)
    for i in range(n):
        hash = set()
        for j in range(i+1,n):
            third = -(arr[i] + arr[j])
            if third in hash:
                temp_list = [arr[i], arr[j], third]
                temp_list.sort()
                temp_trip.add(tuple(temp_list))
            hash.add(arr[j])
            
    
    ans = list(temp_trip)
    print(f"all triplets are: {ans}")
    return None

arr = [-1,0,1,2,-1,-4]
sum_3(arr)

# T.C = O(n^2)
# S.C = O(no. of triplets) + o(n)