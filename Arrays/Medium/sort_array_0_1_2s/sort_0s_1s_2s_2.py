# This function is to sort the given array which contains only 0s,1s and 2s using counter approach:


# Pseudo Code:
"""
arr = [0,1,2,0,1,2,1,2,0,0,0,1]

create 2 counters
iterate the loop and count all 
based on the counts run the loop and replace the values.
"""

# Implementation : 

def sort_array(arr):
    cnt0, cnt1, cnt2 = 0,0,0
    for i in range(len(arr)):
        if arr[i] == 0: 
            cnt0+=1
        elif arr[i] == 1:
            cnt1+=1
        else:
            cnt2+=1
    print(f"{cnt0}\n{cnt1}\n{cnt2}")
    for i in range(cnt0):
        arr[i] = 0
    for j in range(cnt0,(cnt0+cnt1)):
        arr[j] = 1
    for k in range((cnt0+cnt1),(cnt0+cnt1+cnt2)):
        arr[k] = 2
    return arr

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
result = sort_array(arr)
print(f"result of the unsorted array is : {result}")

# T.C = O(2n) => o(n) + o(cnt0) + o(cnt1) + o(cnt2)
# S.C = O(1)