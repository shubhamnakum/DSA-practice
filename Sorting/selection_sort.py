# This function is to sort the array using selection sort

# Psuedo Code: 
"""
arr=[13,46,24,52,20,9]

for (i=0 --> n-2)
{
    min  = i
    for(j=i,j<=n-1;j++)    
    {
        if (a[i]<a[min]):
            min = i
    }
    swap(a[i],a[min])
}
"""

# Implementation : 

def selection_sort(arr, n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if (arr[j] < arr[min]):
                min = j

        # Swap
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    
    return arr

arr = [13,46,24,52,20,9]
n = len(arr)
sorted_arr = selection_sort(arr,n)
print(f"Unsorted array : {arr} \nSorted array is : {sorted_arr}")


# T.C --> O(n2)
# S.C --> o(1)