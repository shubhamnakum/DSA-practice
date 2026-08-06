# This function is to find the intersection of 2 sorted arrays using the bruteforce approach:

# Pseudo code:
"""
a1 = [1,2,2,3,3,4,5,6]
a2 = [2,3,3,5,6,6,7]

intersection(a1,a2):
    create a visited = [] of min size arrays
    run a nested loop and see if both element match and if they are already visted or not.
    if not then append it
"""


# implementation:

def intersection(a1,a2):
    n1 = len(a1)
    n2 = len(a2)
    visited = [0] * min(n1,n2)
    intersect = []
    for i in range(n1):
        for j in range(n2):
            if a1[i] == a2[j] and visited[j] == 0:
                intersect.append(a1[i])
                visited[j]=1
                break
            if  a2[j] > a1[i]:
                break

    return intersect

a1 = [1,2,2,3,3,4,5,6]
a2 = [2,3,3,5,6,6,7]
result = intersection(a1,a2)
print(f"intersection of 2 arrays are : {result}")


# T.C = O(n1*n2)
# S.C = o(n2)  // minimum sized array