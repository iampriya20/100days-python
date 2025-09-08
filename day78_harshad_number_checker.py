def is_harshad(n: int) -> bool:
    if n <= 0:
        return False
    s = 0
    x = n
    while x:
        s += x % 10
        x //= 10
    return n % s == 0

try:
    n = int(input("Enter a positive integer: ").strip())
    print("Harshad (Niven) Number" if is_harshad(n) else "Not a Harshad Number")
except ValueError:
    print("Invalid input. Please enter an integer.")
