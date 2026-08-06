# This Function is to remove duplicate elements from the sorted array, in-place.
# Bruteforce Approach


# Psuedo Code:
"""
arr = [1,1,2,2,2,3,3,4]

remove_dups(arr):
    push each elemnets into a set, this will remove the dups
    and then reassign in the same arr from set

    arr = set(arr)
    return

"""

# Implementation:

def remove_dups(arr):
    arr = {ele for ele in arr}
    return arr


arr = [1,1,2,2,2,3,3,4,4,4,6,6,9,8,8]
unique_arr = remove_dups(arr)
print(f"Unique elements in the array are :{unique_arr}")


# T.C = o(n)
# S.c = o(1)