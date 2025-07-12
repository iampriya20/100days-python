# day19_swap_variables.py

# Ask user for two values
a = input("Enter the first value (a): ")
b = input("Enter the second value (b): ")

print(f"Before swapping → a = {a}, b = {b}")

# Swap without using a temporary variable
a, b = b, a

print(f"After swapping  → a = {a}, b = {b}")
