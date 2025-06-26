# Day 3 - Number Type and Odd/Even Checker using if-elif-else

# Get user input
num = float(input("Enter a number: "))

# Check type of number
if num > 0:
    print("It is a Positive number.")
elif num < 0:
    print("It is a Negative number.")
else:
    print("The number is Zero.")

# Check if it's a whole number before checking odd/even
if num.is_integer():
    if int(num) % 2 == 0:
        print("It is an Even number.")
    else:
        print("It is an Odd number.")
else:
    print("It is not a whole number, so Odd/Even check doesn't apply.")
