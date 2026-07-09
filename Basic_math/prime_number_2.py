# This function is to check if the number is a prime number or not:
import math as m

# Pseudo Code: 
"""
N=...
for (i=1,i<=sqrt(N),i++)
{
    if (N % i)==0:
        count++
        if ((N/i)!=1):
            count++
    if count == 2:
        is_prime    
}
"""

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
                
    return is_prime_number

n = int(input("Enter a number "))
result = is_prime(n)
print(f"Is the number {n}, a prime number? --> {result}")



# Time Complexity : o(sqrt(n))