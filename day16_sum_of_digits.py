# Day 16: Sum of Digits of a Number

num = input("Enter a number: ")
digit_sum = 0

for digit in num:
    if digit.isdigit():
        digit_sum += int(digit)

print(f"The sum of digits in {num} is {digit_sum}")
