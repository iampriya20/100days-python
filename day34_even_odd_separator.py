# day34_even_odd_separator.py

numbers = input("Enter numbers separated by spaces: ").split()

even = []
odd = []

for num in numbers:
    if num.isdigit():
        n = int(num)
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

print(f"\n✅ Even numbers: {even}")
print(f"✅ Odd numbers: {odd}")
