# from the given array, find the longest consecutive sequence using bruteforce approach

# Pseudo code:
""" 
arr = [102,4,100,1,101,3,2,1,1]

using nested loops take each element and see if the (ele+1) exists or not and update the count
"""

# Implementation:

def lcs(arr):
    longest = 1
    for ele in arr:
        x = ele
        cnt = 1
        while ((x+1 in arr) == True):
            cnt+=1
            x = x+1
        longest = max(longest,cnt)
    print(f"longest consecutive subsequence is : {longest}")
    return None

arr = [102,4,100,1,101,3,2,1,1]
lcs(arr)

# T.C = O(n^2)
# S.C = O(1)