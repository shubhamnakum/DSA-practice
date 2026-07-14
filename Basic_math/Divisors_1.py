# This is Function to find the divisors of a number

# Puesdocode:
"""
N = 36 
for (i=1, i<=N, i++)
{
    if (N %i ==0)}
    {
        print(i)
    }
}
"""

def find_divisors(num):

    divisor_list = []
    for i in range (1,num+1):
        if (num % i == 0):
            divisor_list.append(i)
    return divisor_list

n = int(input("Enter a Number: "))
result = find_divisors(n)
print(f"Divisors of {n} are {result}")


# Time Complexity : O(num)