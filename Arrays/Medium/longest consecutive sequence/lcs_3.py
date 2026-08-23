# from the given array, find the longest consecutive sequence using set data structure:
""" 
arr = [102,4,100,1,101,3,2,1,1]

insert the elements in to a set
iterate the set and check if ele-1 exist in set or not 
if exist then ele is not starting point so move to next element
if ele-1 not exist then its starting point so now check next element exists or not and update the counts

""" 

# Implementation:

def lcs(arr):
    longest = 1
    cnt = 1
    hash_set = set(arr)
    for ele in hash_set:
        if ele-1 not in hash_set:
            cnt = 1 
            while (ele+1 in hash_set) == True:
                ele = ele+1
                cnt+=1
            longest = max(longest,cnt)
    print(f"longest consecutive subsequence is : {longest}")
    return None

arr = [102,4,100,1,101,3,2,1,1]
lcs(arr)

# T.C = o(n)+o(n+n) = o(n)
# S.C = O(n)