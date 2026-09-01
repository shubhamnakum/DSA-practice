# given an array, find the triplets that sums upto 0 using optimal approach

# Pseudo Code:
""" 
arr = [-1,0,1,2,-1,-4]

using 2 pointers approach

we sort the array and then iterate i and have 2 pointers j and k 
if sum is < 0  then inc j
if sum is > 0 then dec k
if summ = 0 then triplet
"""

# Implementation: 

def sum_3(arr):
    ans = set()
    arr.sort()
    n = len(arr)
    for i in range(n):
        j = i+1
        k = n-1
        while (j<k):
            sum = arr[i]+arr[j]+arr[k]
            if sum < 0:
                j+=1
            elif sum > 0:
                k-=1
            else:
                temp_list = [arr[i],arr[j],arr[k]]
                ans.add(tuple(temp_list))
                j+=1
                k-=1
                while (j<k and arr[j]==arr[j-1]):
                    j+=1
                while (j<k and arr[k]==arr[k+1]):
                    k+=1
            

    print(f"all triplets are: {ans}")
    return None

arr = [-1,0,1,2,-1,-4]
sum_3(arr)

# T.C = O(n^2)
# S.C = O(no. of triplets) + o(1)