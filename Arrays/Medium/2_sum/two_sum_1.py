# This function is to find the two elements that sums upto the given target, using bruteforce approach:

# Pseudo Code:
"""
a=[2,6,8,5,11]

run a loop from 0,n:
    run another loop from i to n:
        if sum of arr(i,j) == target: 
            return i,j
"""


# implementation:

def two_sum(a,target):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j] == target:
                return i,j

a = [2,6,8,5,11]
target = 14
id_1,id_2 = two_sum(a,target)
print(f"the indices are: {id_1} & {id_2}")


# T.C = o(n2)
# S.C = o(1)