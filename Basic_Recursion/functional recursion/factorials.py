# This is a Function to find factorials of N using Functional Recursion


# Psuedo Code
"""
fact(n):
    if n is 1:
        return 1
    return n * fact(n-1)    // current number * fact of all prev numbers

main():
n=3
result = fact(n)

"""

# Implementation:

def fact(n):
    if (n==1):
        return 1
    return n * fact(n-1)

n = int(input("Enter a Number n: "))
result = fact(n)
print(f"Fcatorial of {n} is {result}")

# T.C = O(n)