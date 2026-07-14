# This function is to find all prime numbers between N.
import math as m
# Psuedo Code: 
"""
prime_list[n+1] 
for (i = 2 -> n):
     prime_list[i] = 1 // initialize a list of size n with 1
for (i = 2, i*i <=N, i++) // loop till sqrt(n)
    if (prime_list[i]==1):
        for(j=i*i, j<=n, j+=i):
            prime_list[j] = 0
for (i=2->n):
    if prime_list[i] == 1:
        print(i)
"""


# Implementation:

def find_primes(n):

    # initialize a list of size n with 1
    prime_list = [1] * (n+1)
    result = []

    # 0 and 1 are not prime
    prime_list[0] = prime_list[1] = 0

    for i in range(2, int(m.sqrt(n))+1):
        if (prime_list[i]==1):
            for j in range (i*i,n+1, i):
                prime_list[j] = 0
    
    for i in range(2,n+1):
        if prime_list[i] == 1:
            result.append(i)
    return result

n = int(input("Enter a Number to find all prime till that number : "))
result = find_primes(n)
print(f"All Primes till {n} are {result}")

# T.C : O(log(log n))