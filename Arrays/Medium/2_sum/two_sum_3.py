# This function is to find the two elements that sums upto the given target, using Hashing approach:

# Pseudo Code:
"""
a=[2,6,8,5,11]


for i = 0 --> n:
    rem = target - sum
    if rem in hash:
        return [hash[map]],i]
    hash[arr] = i
    retutn []
"""


# implementation:

def two_sum(a,target):
    n=len(a)
    hash = {}
    for i in range(n):
        sum = a[i]
        rem = target - sum
        if rem in hash:
            return (hash[rem],i)
        hash[a[i]] = i
    return -1,-1


a = [2,6,8,5,11]
target = 14
id_1,id_2 = two_sum(a,target)
print(f"the indices are: {id_1} & {id_2}")


# T.C = o(n)
# S.C = o(n)