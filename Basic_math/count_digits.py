# Function for counting number of digits in a number:

def count_digits(num):
    initial_num = num
    count = 0
    while num  > 0:
        last_digit = num % 10
        count = count + 1
        num = int(num/10)
    print(f"Total no. of digits in {initial_num} is {count}.")
    return None

n = int(input("Enter a Number : "))
count_digits(n)