def digital_root(n: int) -> int:
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

try:
    n = int(input("Enter a positive integer: ").strip())
    print("Digital Root:", digital_root(n))
except ValueError:
    print("Invalid input. Please enter an integer.")
