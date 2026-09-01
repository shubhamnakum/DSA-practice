# given an array, find the triplets that sums upto 0 using bruteforce approach.

# Pseudo Code:
""" 
arr = [-1,0,1,2,-1,-4]

using naive nested loop approach
"""

# Implementation: 

def sum_3(arr):
    temp_trip = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp_list = [arr[i],arr[j],arr[k]]
                    temp_list.sort()
                    temp_trip.add(tuple(temp_list))
    
    ans = list(temp_trip)
    print(f"all triplets are: {ans}")
    return None

arr = [-1,0,1,2,-1,-4]
sum_3(arr)

# T.C = O(n^3)
# S.C = O(no. of triplets)