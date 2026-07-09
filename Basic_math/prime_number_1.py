# This function is to check if the number is a prime number or not:

# Pseudo Code: 
"""
N=...
for (i=1,i<=N,i++)
{
    if (N % i)==0:
        count++
    if count == 2:
        is_prime    
}
"""

def is_prime(num):
    count=0
    for i in range(1,num+1):
        if (num % i) == 0 :
            count+=1
        if count == 2:
            isnum_prime = True
        else:
            isnum_prime = False
    return isnum_prime

n = int(input("Enter a number "))
result = is_prime(n)
print(f"Is the number {n}, a prime number? --> {result}")


# Time Complexity : O(num)