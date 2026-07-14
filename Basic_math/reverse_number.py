# Function is about reversing a number:

# Pesudo code:
"""
N = some number
rev_num = 0 (initially)

while (N>0):
    last_digit = N % 10
    rev_num = (rev_num * 10) + last_digit
    N = int(N / 10)

return rev_num
"""

# Function : 

def reverse_number(num):
    initial_num = num 
    rev_num = 0
    while (num > 0):
        last_digit = num % 10
        rev_num = (rev_num * 10) + last_digit
        num = int(num / 10)
    print(f"Reverse of the number, {initial_num} is {rev_num}")
    return None

n = int(input("Enter a Number : "))
reverse_number(n)

# Time Complexity : O(log10(N))+1, because the loop runs once per digit, and the number of digits is proportional to log n.
# Input: 
# n=12345
# Digits = 5
# log10 (12345) ≈ 4.09, add 1 → 5 iterations.