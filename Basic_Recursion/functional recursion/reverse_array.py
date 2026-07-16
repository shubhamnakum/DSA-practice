# This is a Function to reverse an array of size N using Functional Recursion


# Psuedo Code
"""
func(i, list, n):
    if(i>=(n/2)):
        return
    swap(a[i],a[n-i-1])
    func(i+1,list,n)

main():
list = [1,2,3,4,5]
n = len(list)
result = func(0,list,n)

"""

# Implementation:

def func(i,ls,n):
    if (i>= (n/2)):
        return
    
    # Swap the numbers
    temp = ls[i]
    ls[i] = ls[n-i-1]
    ls[n-i-1] = temp

    return func(i+1,ls,n)


n = int(input("Enter a size of array: "))
list = []
for i in range(1,n+1):
    list.append(i)
func(0,list,n)
print(f"{list}")

# T.C = O(n/2)
# S.C = O(n/2) --> due to stack space
