# This function returns the majority elements from the given array, if the element is > n/3 times then it is majority element.

# Brute force:

# Pseudo code:
""" 
arr = [1,1,1,1,3,2,2,2]

iterate element and if the count is >n/3
"""

# Implementation:

def maj_ele(arr):
    ans = []
    for i in range(len(arr)):
        if len(ans) == 0 or ans[0]!=arr[i]:
            cnt = 0
            for j in range(len(arr)):
                if arr[j] == arr[i]:
                    cnt+=1
            if cnt > len(arr)//3:
                ans.append(arr[i])

        if len(ans) == 2:
            break
            
    print(f"majority elements in the array are:{ans}")
    return None

arr = [1,1,1,1,3,2,2,2]
maj_ele(arr)

# T.C = O(n^2)
# S.C = O(1)