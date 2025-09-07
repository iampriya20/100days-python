def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    s = 1  # 1 is a proper divisor of all n >= 2
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            j = n // i
            if j != i:  # avoid double-adding the square root
                s += j
        i += 1
    return s == n

try:
    n = int(input("Enter a positive integer: ").strip())
    print("Perfect Number" if is_perfect(n) else "Not a Perfect Number")
except ValueError:
    print("Invalid input. Please enter an integer.")
