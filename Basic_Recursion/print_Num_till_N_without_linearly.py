# This Function is to print all numbers till N times without linear operation(i.e: i++) using Recursion

# Psuedo Code: 
"""
n = 5

func(i,n):
{
    if (i<1):
        return
    func(i-1,n)
    print(i)
}

main():
n=5,i=n
func(i,n)
"""


# Implementation: 

def func(i,n):
    if (i<1):
        return
    func(i-1,n)
    print(i)
    return None

n = int(input("Enter the number: "))
i = n
func(i,n)

# T.C : O(n)
# Stack Space : O(n)