# This function is to sort the given array which contains only 0s,1s and 2s using dutch national flag approach:


# Pseudo Code:
"""
arr = [0,1,2,0,1,2,1,2,0,0,0,1]

low,mid,high = 0,0,n-1

while (mid<=high):
    if arr[mid] == 0 :
        swap(arr[low],arr[mid])
        mid++
        low++
    elif arr[mid] == 1:
        mid++
    else: 
        swap(arr[high],arr[mid])
        high--
"""

# Implementation : 

def sort_array(arr):
    low,mid,high = 0,0,(len(arr)-1)

    while (mid<=high):
        if arr[mid] == 0 :
            arr[low],arr[mid] = arr[mid],arr[low]
            mid+=1
            low+=1
        elif arr[mid] == 1:
            mid+=1
        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high-=1
    return arr

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
result = sort_array(arr)
print(f"result of the unsorted array is : {result}")

# T.C = O(n)
# S.C = O(1)