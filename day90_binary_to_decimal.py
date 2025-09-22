# Day 90: Binary to Decimal Converter

def binary_to_decimal(binary_str: str) -> int:
    """Convert a binary string to decimal without using int(x, 2)."""
    decimal = 0
    power = 0
    for digit in binary_str[::-1]:  # reverse to process from right to left
        if digit not in ("0", "1"):
            raise ValueError("Invalid binary number")
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal


if __name__ == "__main__":
    binary = input("Enter a binary number: ")
    try:
        print(f"Decimal representation of {binary} is {binary_to_decimal(binary)}")
    except ValueError as e:
        print(e)
