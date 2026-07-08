# Function is about checking a number is palindrome or not:

# Pesudo code:
"""
N = some number

if N == reverse_N : 
    then Palindrome
else: 
    not a palindrome
"""

# Function : 

def is_palindrome(num):
    num_org = num
    is_palindrome = None

    rev_num = 0
    while (num > 0):
        last_digit = num % 10
        rev_num = (rev_num * 10) + last_digit
        num = int(num / 10)

    if num_org == rev_num:
        isnum_palindrome = True
    else:
        isnum_palindrome = False
    return isnum_palindrome

n = int(input("Enter a Number : "))
result = is_palindrome(n)
print(f"is number {n}, a Palindrome? --> {result}")

# Time Complexity : O(log10(N))+1, because the loop runs once per digit, and the number of digits is proportional to log n.
# Input: 
# n=12345
# Digits = 5
# log10 (12345) ≈ 4.09, add 1 → 5 iterations.