# This function returns the majority elements from the given array, if the element is > n/3 times then it is majority element.

# extended Moore's Voting algorithm:

# Pseudo code:
""" 
arr = [1,1,1,1,3,2,2,2]

using moore's algo, here we will maintain 2 candidates and their counts.
with each element we check if ele is cand1 or cand2 if so increase their count
else decrease both their counts. 
once done do 2nd pass and get the counts of both candidates and verify with cond.
"""

# Implementation:

def maj_ele(arr):
    ans = []
    cand1 = float("-inf")
    cand2 = float("-inf")
    cnt1,cnt2 = 0,0
    # pass 1: find possible candidates
    for ele in arr:
        if ele == cand1:
            cnt1+=1
        elif ele == cand2:
            cnt2+=1
        elif cnt1 == 0:
            cand1 = ele
            cnt1+=1
        elif cnt2 == 0:
            cand2 = ele
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
            
    # Pass 2: verify the possible candidates
    for ele in arr:
        if ele == cand1:
            cnt1 +=1
        elif ele == cand2:
            cnt2 +=1
    
    if cnt1 > len(arr)//3:
        ans.append(cand1)
    if cnt2 > len(arr)//3:
        ans.append(cand2)
        
    print(f"majority elements in the array are:{ans}")
    return None

arr = [1,1,1,1,3,2,2,2]
maj_ele(arr)

# T.C = O(n) + O(n) = O(2n)
# S.C = O(1)