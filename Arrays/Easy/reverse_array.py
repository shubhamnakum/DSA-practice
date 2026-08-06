# This function is to reverse an array

# Psuedo Code: 
"""
a = [1,2,3,4,5]

def reverse(a):
    start = 0
    end = len(a)-1
    while(start <= end):
        swap(a[start],a[end])
        start ++
        end --
"""

def reverse(arr):
    start = 0
    end = len(arr) -1
    while (start<=end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
    return arr

arr = [1,2,3,4,5]
result = reverse(arr)
print(f"reversed array is : {result}")

# T.C = o(n)
# S.C = o(1)