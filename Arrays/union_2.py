# This Function is to find union of two sorted arrays using 2 pointer apporach:

# Psuedo code:
"""
a1= [1,1,2,3,4]
a2 = [2,3,4,4,5,6]

union(a1,a2):
    we take 2 pointers one for each array.
    compare both ele and add the min element in the union and increment the pointer.

"""

# Implementation:

def union(a1,a2):
    union_arr = []
    i,j=0,0
    n1 = len(a1)
    n2 = len(a2)

    while(i<n1 and j<n2):
        # if i is duplicate element the skip it
        if i>0 and a1[i] == a1[i-1]:
            i+=1
            continue

        # if j is duplicate element then skip it
        if j>0 and a2[j] == a2[j-1]:
            j+=1
            continue

        # compare both ith and jth element and append in the union_arr
        if a1[i] < a2[j]:
            union_arr.append(a1[i])
            i+=1
        elif a2[j] < a1[i]:
            union_arr.append(a2[j])
            j+=1
        else:
            union_arr.append(a1[i])
            i+=1
            j+=1

    # add the remaining elements:
    while (i<n1):
        if i == 0 or a1[i]!=a1[i-1]:
            union_arr.append(a1[i])
        i+=1
    while (j<n2):
        if j == 0 or a2[j]!=a2[j-1]:
            union_arr.append(a2[j])
        j+=1    

    return union_arr

a1 = [1,1,2,3,4]
a2 = [2,3,4,4,5,6,6,7,9]
result = union(a1,a2)
print(f"union of two array is: {result}")

# T.C = o(n1 + n2)
# S.C = o(n1+n2)