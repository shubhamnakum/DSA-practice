# This function is to sort an array using the Bubble sort algorithm.

# Psuedo Code : 
"""
arr = [13,46,24,52,20,9]

for i = n-1 --> >=1:
    did_swap = 0
    for j = 0 --> i:
        if arr[j] > arr[j+1]:
            swap (arr[j],arr[+1])
            did_swap = 1
    if did_swap = 0:
        break
"""


# Implementation:

def bubble_sort(arr):
    n = len(arr)
    is_swap = 0
    for i in range(n-1,0,-1):
        for j in range(i):
            if (arr[j] > arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                is_swap = 1
    if is_swap == 0:
        return 
    print("inside")
    print(f"sorted array : {arr}")
    return arr

arr = [13,46,24,52,20,9]
sorted_arr = bubble_sort(arr)
print(f"sorted array : {sorted_arr}")


# T.C = o(n^2)
# S.C = o(1)