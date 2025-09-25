# Day 93: Decimal to Octal Converter

def decimal_to_octal(n: int) -> str:
    """Convert a decimal number to octal without using oct()."""
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal


if __name__ == "__main__":
    num = int(input("Enter a decimal number: "))
    print(f"Octal representation of {num} is {decimal_to_octal(num)}")
