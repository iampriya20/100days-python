# Day 5 - Multiplication Table using while loop

# Ask user for a number
number = int(input("Enter a number to generate its multiplication table: "))
i = 1

# Loop from 1 to 10
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
