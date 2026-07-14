# This function is to find the GCD / HCF of 2 numbers.
# Euclidean approach:

# Psuedo Code
"""
N1 = 9, N2 = 12

while (N1>0 & N2>0)
{
    if(N1>N2)}
        N1=N1%N2
    else
        N2=N2%N1
}
if N1==0
    gcd = N1
else
    gcd = N2
"""

def find_gcd(num1,num2):
    a=num1
    b=num2
    while (a>0) & (b>0):
        if (a>b):
            a=a%b
        else:
            b=b%a
    print(f"a = {a}, b={b}")
    if a==0:
        gcd = b
        return gcd
    elif b==0:
        gcd = a
        return gcd

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))

result = find_gcd(n1,n2)
print(f"GCD of  {n1} & {n2} is, {result}")

# Time Complexity : O(log(min(a,b))) [base phi]