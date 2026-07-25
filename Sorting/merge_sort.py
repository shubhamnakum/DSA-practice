# This function is to sort an array using merge sort.

# Pseudo Code:
"""
arr = [3,1,2,4,1,5,2]

low = arr[0], high = arr[-1]
def merge_sort(arr,low, high):
    if (low >= high) :              // if only one element then return the arr
        return arr
    mid = (low + high)//2
    merge_sort(arr,low,mid)         // divide the array
    merge_sort(arr,mid+1,high)  
    merge(arr,low,mid,high)         // sort & merge array
    return arr

def merge(arr,low,mid,high):
    left = low, right = mid+1
    temp = []

    while(left<=mid && right <= mid):     // sort & merge the array into temp
        if (arr[left]<=arr[right]):
            temp.append(arr[left])
            left++
        else:
            temp.append(arr[right])
            right++

    while (left<=mid):                   // append the remaining elements from left array if any
        temp.append(arr[left])
        left++
    
    while (right<=mid):                   // append the remaining elements from right array if any
        temp.append(arr[right])
        right++
    
    arr = temp                             // assign the temp array in arr.
    
"""


# Implementation:

def merge(arr,low,mid,high):
    left,right = low,mid+1
    temp = []
    while(left<=mid and right<=high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1
    arr[low:high+1] = temp
    return arr


def merge_sort(arr,low,high):
    if (low>=high):
        return arr
    mid = int((low+high)/2)
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    return merge(arr,low,mid,high)


arr = [3,4,2,1,6,5]
low,high =0, len(arr)-1
sorted_arr = merge_sort(arr,low,high)
print(f"Sorted Array : {sorted_arr}")


# T.C = o(N*Log2N) --> total
# T.C (divide) --> O(Log2N)
# T.C (sort & merge) --> o(N)
