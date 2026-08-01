# This function is to  find maximum consecutive ones in the array using bruteforce approach

# Pseudo Code:
"""
arr = [1,1,0,1,1,1,0,1,1]

max,cnt = 0
for i=0 --> n-1:
    if arr[i] == 1:
        cnt += 1
        max = max(max,cnt)
    else:
        cnt = 0
return max
"""

def max_ones(arr):
    maxi,cnt = 0,0
    for i in range(0,len(arr)):
        if arr[i] == 1:
            cnt += 1
            maxi = max(maxi,cnt)
        else:
            cnt = 0
    return maxi

arr = [1,1,0,1,1,1,0,1,1]
result = max_ones(arr)
print(f"max consecutive ones are : {result}")

# T.C = o(n)
# S.c = o(1)