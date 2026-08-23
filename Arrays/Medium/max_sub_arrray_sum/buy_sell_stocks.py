# This function is to identify the best day to buy & sell stocks so that profit is maximum.

# Pseudo Code:
"""
arr = [7,1,5,2,6,4]

min_i = arr[0], profit = 0
for i =1 --> n:
    cost = arr[i] - min_i
    profit = max(profit,cost)
    min_i = min(min_i,arr[i])
return profit
"""

# Implementation:

def max_profit(arr):
    mini = arr[0]
    profit = 0
    for i in range(len(arr)):
        cost = arr[i]-mini
        profit = max(profit,cost)
        mini = min(mini,arr[i])
    return profit

arr = [7,1,5,2,6,4]
result = max_profit(arr)
print(f"Max profit is: {result}")

# T.C = o(n)
# S.C = o(1)