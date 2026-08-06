# This Function is to move all zeros to end using bruteforce approach:

# Pseudo code:
"""
arr = [1,2,4,0,0,5,1,0,1]

move_zeros(arr):
    1. load the non-zeros in to temp array
    2. add/replace the temp array to the original array
    3. fill the remaining with zero in the original array
"""

def move_zeros(arr):
    temp = []

    print(f"arr initially : {arr}")
    # 1. load the non-zeros in the temp array
    for ele in arr:
        if ele != 0:
            temp.append(ele)

    nt = len(temp)
    # 2. Fill the temp array in the original array
    for i in range(0, nt):
        arr[i] = temp[i]
    print(f"array after 2. {arr}\n size: {len(arr)}")

    # 3. fill the remaining with zeros
    for i in range(nt,len(arr)):
        arr[i] = 0
    return arr


arr = [1,2,4,0,0,5,1,0,1]
result = move_zeros(arr)
print(f"resultant array is : {result}")

# T.C = O(2n)
# S.C = o(nt)