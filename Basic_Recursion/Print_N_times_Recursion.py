# This Function is to print text N times using Recursion

# Psuedo Code: 
"""
n = 5

func(i,n):
{
    if (i>n):
        return
    print(Text)
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
    print("Hello World!")
    func(i+1,n)
    return None

n = int(input("Enter the number you want the text to Repeat till: "))
i = 1
func(i,n)

# T.C : O(n)
# Stack Space : O(n)