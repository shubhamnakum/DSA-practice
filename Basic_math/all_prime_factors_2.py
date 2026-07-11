# This fucntion is to find all the prime factors using Direct prime Factorization:

import math as m

# Psuedo code
"""
n = some number

for ( i=2, i<=sqrt(n), i++):
    if (n%i == 0):
        list.append(i)
        while(n%i == 0):
            n = n/i
if (n!=1):
    list.append(n)
"""

# Implementation:

def find_prime_factors(n):
    list = []
    for i in range(2,int(m.sqrt(n))+1):        # T.C --> O(sqrt(n))
        if(n%i == 0):
            list.append(i)
            while(n%i == 0):              # T.C --> O(log(n))
                n=int(n/i)
    if(n!=1):
        list.append(n)
    return list

n = int(input("Enter a Number, "))
result = find_prime_factors(n)
print(f"Prime Factors of {n} are, {result}")


# T.C = O(sqrt(n)*log(n))