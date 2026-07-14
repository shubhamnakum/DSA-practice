# This function is to find the GCD / HCF of 2 numbers.
# Reverse looking approach:

# Psuedo Code
"""
N1 = 9, N2 = 12

for (i=min(N1,N2), i>0, i++)
{
    if ((( N1 % i)==0) & ((N2 % i)==0)):
        GCD = i
        break
}
"""

def find_gcd(num1,num2):
    a=num1
    b=num2

    for i in range(min(a,b),0,-1):
        if (((a%i)==0) & ((b%i)==0)):
            gcd = i
            break
    return gcd

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

result = find_gcd(n1,n2)
print(f"GCD of  {n1} & {n2} is, {result}")

# Time Complexity : O(min(a,b))