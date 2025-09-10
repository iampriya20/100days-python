def is_kaprekar(n: int) -> bool:
    if n < 1:
        return False
    sq = n * n
    s = str(sq)
    d = len(str(n))
    right = int(s[-d:]) if d <= len(s) else int(s)
    left = int(s[:-d]) if s[:-d] else 0
    return left + right == n

try:
    n = int(input("Enter a positive integer: ").strip())
    print("Kaprekar Number" if is_kaprekar(n) else "Not a Kaprekar Number")
except ValueError:
    print("Invalid input. Please enter an integer.")
