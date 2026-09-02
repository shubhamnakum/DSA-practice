# given an array, find the quadralets that sums upto target using 2 pointers approach

# Pseudo Code:
""" 
arr = [-1,0,1,2,-1,-4]

using 2 pointers approach

we sort the array and then iterate i,j and have 2 pointers k and l
if sum is < target  then inc k
if sum is > target then dec l
if summ = target then quad
"""

# Implementation: 

def sum_3(arr,target):
    ans = set()
    arr.sort()
    n = len(arr)
    for i in range(n):
        if (i>0 and arr[i]==arr[i-1]):
            continue
        for j in range(i+1,n):
            if (j>i+1 and arr[j]==arr[j-1]):
                continue
            k = j+1
            l = n-1
            while (k<l):
                sum = arr[i]+arr[j]+arr[k]+arr[l]
                if sum < target:
                    k+=1
                elif sum > target:
                    l-=1
                else:
                    temp_list = [arr[i],arr[j],arr[k],arr[l]]
                    ans.add(tuple(temp_list))
                    k+=1
                    l-=1
                    while (k<l and arr[k]==arr[k-1]):
                        k+=1
                    while (k<l and arr[l]==arr[l+1]):
                        l-=1
                

    print(f"all quads are: {ans}")
    return None

arr = [-1,0,1,2,-1,-4]
target = 1
sum_3(arr,target)

# T.C = O(n^3)
# S.C = O(no. of quads)*2 + o(1)