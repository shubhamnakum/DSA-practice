# This function is to sort an array using quick sort.

# Pseudo Code: 
"""
arr = [4,6,2,5,7,9,1,3]

quicksort(arr,low,high):
    if (low < high):
        p_index = partition(arr,low,high)
        quicksort(arr,low,p_index-1)
        quicksort(arr,p_index+1,high)

partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while(i<j):
        while(arr[i]<=arr[pivot] && i<=high):
            i++
        while(arr[j]>arr[pivot] && j>low):
            j--
        if (i<j):
            swap(arr[i],arr[j])
    swap (arr[low],arr[j]) // swap pivot and r
    return j

"""

# Implementation:

def partition(arr,low,high):
    pivot = arr[low]
    l = low
    r = high
    while (l<r):
        while(arr[l]<=pivot and l<=high):
            l+=1
        while(arr[r]>pivot and r>=low):
            r-=1
        if (l<r):
            arr[l],arr[r] = arr[r],arr[l]
    arr[low], arr[r] = arr[r], arr[low]
    return r

def quicksort(arr,low,high):
    if low < high:
        pindex = partition(arr,low,high)
        quicksort(arr,low,pindex-1)
        quicksort(arr,pindex+1,high)


arr = [4,6,2,5,7,9,1,3]
quicksort(arr,0,len(arr)-1)
print(f"sorted array: {arr}")


# T.C = o(nlogn) // best/average
# T.C = o(n^2) // worst

# S.C = o(n)