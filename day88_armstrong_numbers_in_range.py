# Prints all Armstrong (narcissistic) numbers in the inclusive range [L, R].
def is_armstrong(x: int) -> bool:
    if x < 0:
        return False
    s = str(x)
    p = len(s)
    return x == sum(int(ch) ** p for ch in s)

try:
    L = int(input("Enter start (L): ").strip())
    R = int(input("Enter end (R): ").strip())
    if L > R:
        L, R = R, L
    ans = [n for n in range(L, R + 1) if is_armstrong(n)]
    print("Armstrong numbers:", ans)
except ValueError:
    print("Invalid input. Please enter integers.")
