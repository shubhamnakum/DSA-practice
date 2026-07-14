# This fucntion is to find the value of a number for the given power

# Psuedo Code:
"""
x=2 , n=5
ans=1
while(n>0):
    if (n%2==1):
        ans=ans*x
        n=n-1
    else:
        x=x*x
        n=n/2
return ans

"""

# Implementation:

def power(x,n):
    ans = 1
    if n<0:
        x = 1/x
        n = -n
    while(n>0):
        if(n%2==1):
            ans=ans*x
            n=n-1
        else:
            x=x*x
            n=n/2
    return ans

x = float(input("Enter the base value: "))
n = int(input("Enter the intger exponent value: "))
result = power(x,n)
print(f"Power of the x raised to n is, {result}")

# Time Complexity: O(Log2 n)