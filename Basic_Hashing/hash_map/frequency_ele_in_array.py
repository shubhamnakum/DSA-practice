# This is a Function to find frequency of a element in an array using hash map

# Psuedo Code:
"""
arr = [3,23,13,1,1,231]

ele_freq(arr):
    hash_map = {}
    for ele in arr:
        hash_map[ele] = hash_map.get(ele, 0) + 1
    return hash_map
"""

# implementation :

def ele_freq(arr):
    hash_map = {}
    for ele in arr:
        hash_map[ele] = hash_map.get(ele,0) + 1
    return hash_map

arr = [3,23,3,23,13,1,1,231]

freq_map = ele_freq(arr)
print(f"The Frequency of elements in the array: {arr} are \n {freq_map}")


# T.C = O(n)  where n is size of the string
# S.C = O(n) as size remains constant of 26.