# This function is to find the number that appears once and others twices in the array using hashing approach:

# Pseudo code:
"""
a = [1,1,2,3,3,4,4]

once_occured(a):
    create a hash array of size max element+1 not the size of array
    iterate the array and increment the count of element in the hash array
    find the element with count=1 in hash array
"""


# Implementation:
def once_occured(arr):
    maxe = arr[0]
    # 1. find the largest element in the array:
    for ele in arr:
        maxe = max(maxe,ele)

    # 2. create and increment the count in hash array
    hash_arr = [0] * (maxe+1)
    for i in range(len(arr)):
        hash_arr[arr[i]] += 1

    # 3. find the element with count value =1 in hash
    for i in range(len(arr)):
        if hash_arr[arr[i]]  == 1:
            return arr[i]


arr = [1,1,2,3,3,4,4]
result = once_occured(arr)
print(f"the number that only occured once is : {result}")

# T.C = o(3n)
# S.C = O(maxe)