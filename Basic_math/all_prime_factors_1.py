# This fucntion is to find all the prime factors using navie approach:

import math as m

# Psuedo code
"""
n = some number

for (i=2, i<=sqrt(n),i++):
    if (n % i == 0):
        if(isprime(i) == True):
            list.append(i)
    if(n/i != i):
        if(isprime(i) == True):
            list.append(i)
"""

# Implementation:

def is_prime(num):
    count=0
    for i in range(1,int(m.sqrt(num))+1):
        if (num % i) == 0 :
            count+=1
            if ((num/i)!=i):
                count+=1
        if count==2:
            is_prime_number = True
        else:
            is_prime_number = False
                
    return is_prime_number       # T.C = O(sqrt(n))

def find_prime_factors(n):
    list = []
    for i in range(2,int(m.sqrt(n))+1):        # T.C --> O(sqrt(n))
        if(n%i == 0):
            if (is_prime(i)==True):       # T.C --> O(sqrt(n)) 
                list.append(i)
            if(n/i != i):
                if (is_prime(n/i)==True):     # T.C --> O(sqrt(n))
                    list.append(int(n/i))
    return list

n = int(input("Enter a Number, "))
result = find_prime_factors(n)
print(f"Prime Factors of {n} are, {result}")


# T.C = O(sqrt(n)*2*sqrt(n))