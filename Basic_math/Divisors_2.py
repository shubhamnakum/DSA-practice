# This is Function to find the divisors of a number without looping till N
import math as m


# Puesdocode:
"""
N = 36 
for (i=1, i<=sqrt(N), i++)
{
    if (N %i ==0)
    {
        print(i)  --> is 1 factor

        if ((N/i) != i)  // incase 6*6 then 6 is double counted.
        {
            print(N/i) --> N/i is another factor
        }
    }
}
"""

def find_divisors(num):

    divisor_list = []
    n = int(m.sqrt(num))
    for i in range (1,n+1):
        if (num % i == 0):
            divisor_list.append(i)
            if (int(num/i) != i):
                divisor_list.append(int(num/i))
    return sorted(divisor_list)

n = int(input("Enter a Number: "))
result = find_divisors(n)
print(f"Divisors of {n} are {result}")


# Time Complexity : O(sqrt(num))