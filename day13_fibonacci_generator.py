n = int(input("How many Fibonacci numbers do you want? "))

a, b = 0, 1
fib_sequence = []

for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence:")
print(fib_sequence)
