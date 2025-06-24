# Day 5 - Even or Odd Counter

# Get user input
numbers = input("Enter numbers separated by commas: ")

# Convert string to list of integers
num_list = [int(num.strip()) for num in numbers.split(",")]

# Initialize counters
even_count = 0
odd_count = 0

# Loop and count
for num in num_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Output results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
