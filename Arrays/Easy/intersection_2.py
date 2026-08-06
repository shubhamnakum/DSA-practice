# This function is to find the intersection of 2 sorted arrays using the 2 pointer approach:

# Pseudo code:
"""
a1 = [1,2,2,3,3,4,5,6]
a2 = [2,3,3,5,6,6,7]

intersection(a1,a2):
    take 2 pointers, match both elements if match then append and increment both
    else if value of i < j then increment i 
    else if value of j < i then increment j
"""


# implementation:

def intersection(a1,a2):
    n1 = len(a1)
    n2 = len(a2)
    intersect = []
    i,j = 0,0

    while(i<n1 and j<n2):
        if (a1[i] < a2[j]):
            i+=1
        elif (a2[j] < a1[i]):
            j+=1
        else: 
            intersect.append(a1[i])
            i+=1
            j+=1
    return intersect

a1 = [1,2,2,3,3,4,5,6]
a2 = [2,3,3,5,6,6,7]
result = intersection(a1,a2)
print(f"intersection of 2 arrays are : {result}")


# T.C = O(n1+n2)
# S.C = o(n2)  // minimum sized array