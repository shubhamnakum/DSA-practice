# Function to find the last digit of a number

def last_digit(num):
    while num > 0:
        last_digit = (num) % 10
        int_num = int( num / 10)
        print(f"last digit for {num} is {last_digit}")
        num = int_num
    return None

n = int(input("Enter a number: "))
last_digit(n)