# This function is to find the nth fibonacci value using multi-call recursion:


# Pseudo Code: 
"""
fibo series = 0,1,1,2,3,5,8,.....
indexseries =(0,1,2,3,4,5,6......)
where, 
0 is 1st fib val
1 is 2nd fib val
1 is 3rd fib val
2 is 4th fib val

f(n): 
    if (n <= 1):
        return n
    return f(n-1) + f(n-2)

main ():
n = 5
f(n)
"""

# Implementation:

def fib(n):
    if (n <= 1):
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter a Number n: "))
result = fib(n)
print(f"fibonacci value of {n} is {result}")


# T.C = O(2^n)