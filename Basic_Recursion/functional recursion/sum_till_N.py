# This is a Function to find sum of all numbers till N using Functional Recursion


# Psuedo Code
"""
sum(n):
    if n is 0:
        return 0
    return n + sum(n-1)    // current number + sum of all prev numbers

main():
n=3
result = sum(n)

"""

# Implementation:

def sum(n):
    if (n==0):
        return 0
    return n + sum(n-1)

n = int(input("Enter a Number n: "))
result = sum(n)
print(f"Sum of number till {n} is {result}")

# T.C = O(n)