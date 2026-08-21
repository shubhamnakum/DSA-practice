# from the given array, find the longest consecutive sequence using prev state with 1 pass approach

# Pseudo code:
""" 
arr = [102,4,100,1,101,3,2,1,1]

sort the array
maintain prev small_ele and iterate the array once if the ele-1 is small_ele then increase the count
else reset

"""

# Implementation:

def lcs(arr):
    longest = 1
    small_ele = float("-inf")
    cnt = 1
    arr.sort()
    for ele in arr:
        if ele-1 == small_ele:
            cnt+=1
            small_ele = ele
        elif ele-1 != small_ele:
            small_ele = ele
            cnt = 1
        longest = max(longest,cnt)
    print(f"longest consecutive subsequence is : {longest}")
    return None

arr = [102,4,100,1,101,3,2,1,1]
lcs(arr)

# T.C = O(nlogn) + o(n)
# S.C = O(1)