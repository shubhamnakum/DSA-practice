# This function is to sort an array using Insertion sort

# Pseudo code:
"""
arr = [14,9,15,12,6,8,13]

for i=0-->n-1:
    j = i 
    while (j>0 && a[j-1]>a[j]):
        swap (a[j-1],a[j])
        j--
"""

# Implementation

def insertion_sort(arr):
    n = len(arr)
    for i in range(0,n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr

arr = [52,46,39,28,20,12,4]
sorted_arr = insertion_sort(arr)
print(f"sorted array : {sorted_arr}")


# T.C = o(N) -- best case
# T.c = o(N^2) -- Avg/worst case