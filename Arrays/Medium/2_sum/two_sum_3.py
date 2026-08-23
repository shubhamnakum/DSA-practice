# This function is to find the two elements that sums upto the given target, using 2 pointers approach:
# Note: This approach can only check if there exists any 2 number that sums to target, it cant return the indices of it.

# Pseudo Code:
"""
a=[2,6,8,5,11]

a.sort()
l,r = 0,n-1
while(l>r):
    sum = arr(l) + arr(r)
    if  sum == target:
        print(yes)
        break
    else if : sum > target:
        r--
    else if : sum < target:
        l++
"""


# implementation:

def two_sum(a,target):
    a.sort()
    l,r = 0, (len(a)-1)
    while(l<r):
        sum = a[l] + a[r]
        if sum > target:
            r-=1
        elif sum < target:
            l+=1
        else:
            print(f"yes, the sum of {a[l]} and {a[r]} is {sum} that matches the target : {target}")
            break
    return None


a = [2,6,8,5,11]
target = 14
two_sum(a,target)


# T.C = o(n) + o(nlogn)
# S.C = o(1)