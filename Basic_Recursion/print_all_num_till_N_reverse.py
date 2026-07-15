# This Function is to print all numbers till N times in reverse order using Recursion

# Psuedo Code: 
"""
n = 5

func(i,n):
{
    if (i<1):
        return
    print(i)
    func(i-1,n)
}

main():
n=5, i = n
func(i,n)
"""


# Implementation: 

def func(i,n):
    if (i<1):
        return
    print(i)
    func(i-1,n)
    return None

n = int(input("Enter the number: "))
i = n
func(i,n)

# T.C : O(n)
# Stack Space : O(n)