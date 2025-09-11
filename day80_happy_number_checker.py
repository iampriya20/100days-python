def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

try:
    n = int(input("Enter a positive integer: ").strip())
    print("Happy Number" if is_happy(n) else "Not a Happy Number")
except ValueError:
    print("Invalid input. Please enter an integer.")
