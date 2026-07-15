# This Function is to print all numbers till N times using Recursion

# Psuedo Code: 
"""
n = 5

func(i,n):
{
    if (i>n):
        return
    print(i)
    func(i+1,n)
}

main():
i=1,n=5
func(i,n)
"""


# Implementation: 

def func(i,n):
    if (i>n):
        return
    print(i)
    func(i+1,n)
    return None

n = int(input("Enter the number: "))
i = 1
func(i,n)

# T.C : O(n)
# Stack Space : O(n)