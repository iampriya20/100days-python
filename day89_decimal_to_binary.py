# Day 89: Decimal to Binary Converter

def decimal_to_binary(n: int) -> str:
    """Convert a decimal number to binary without using bin()."""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


if __name__ == "__main__":
    num = int(input("Enter a decimal number: "))
    print(f"Binary representation of {num} is {decimal_to_binary(num)}")
