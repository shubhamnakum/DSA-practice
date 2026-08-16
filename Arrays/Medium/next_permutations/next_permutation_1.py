# Find the next Permutation of a given array using the 2 pass:

# Pseudo code:
"""
arr =  [2,1,5,4,3,0,0]

1. find the index where Right to left is not increasing further.
2. swap the element at index with the 1st most element from right that is greater than it.
3. reverse the arr from ind+1 to n-1 (increasing part) to get the smallest sequence of that.
"""

# Implementation:

def permutation(arr):
    ind = 0
    n = len(arr)
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i
            break
    print(f"index iss: {ind}")
    for j in range(n-1,i,-1):
        if arr[j] > arr[ind]:
            arr[j],arr[ind] = arr[ind],arr[j]
            break
    print(f"arr after swap: {arr}")
    arr[ind+1:n] = arr[ind+1:n][::-1]
    return arr

arr = [2,1,5,4,3,0,0]
result = permutation(arr)
print(f"next permutation will be: {result}")

# T.C = o(3n) 2 n's for loop and 1 n for reversal
# S.C = o(1)