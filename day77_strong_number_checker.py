def is_strong(n: int) -> bool:
    if n < 0:
        return False
    # Precompute factorials for digits 0-9
    fact = [1] * 10
    for d in range(2, 10):
        fact[d] = fact[d - 1] * d
    s, x = 0, n
    if x == 0:
        s = fact[0]
    while x > 0:
        s += fact[x % 10]
        x //= 10
    return s == n

try:
    n = int(input("Enter a non-negative integer: ").strip())
    print("Strong Number" if is_strong(n) else "Not a Strong Number")
except ValueError:
    print("Invalid input. Please enter an integer.")
