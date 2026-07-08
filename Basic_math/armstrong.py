# Function is to check whether the number is a Armstrong or not

# Pesudo code : 
"""
n = some number
sum = 0 
d = no. of digits

while n>0:
    last digit = n % 10
    sum = sum + pow((last_digit),d)
    n = int(n/10)

if sum == n:
    Armstrong number
else: 
    Not Armstrong number
"""

def is_armstrong(num):
    sum = 0
    org_num = num
    d = 0 

    while num > 0:
        last_digit = num % 10
        d += 1
        num = int(num / 10)

    num = org_num
    while num > 0:
        last_digit = num % 10
        sum =  sum + pow(last_digit,d)
        num = int(num / 10)
    
    if org_num == sum :
        isnum_armstrong = True
    else:
        isnum_armstrong = False
    
    return isnum_armstrong

n = int(input("Enter a Number : "))
result = is_armstrong(n)
print(f"is the number {n}, a armstrong number ? --> {result}")

# Time Complexity -> O(log n)