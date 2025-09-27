# Day 94: Hexadecimal to Decimal Converter

def hex_to_decimal(hex_str: str) -> int:
    """Convert a hexadecimal string to decimal without using int(x, 16)."""
    hex_str = hex_str.upper()
    digits = "0123456789ABCDEF"
    decimal = 0
    power = 0

    for char in hex_str[::-1]:  # process from right to left
        if char not in digits:
            raise ValueError("Invalid hexadecimal number")
        decimal += digits.index(char) * (16 ** power)
        power += 1

    return decimal


if __name__ == "__main__":
    hex_num = input("Enter a hexadecimal number: ")
    try:
        print(f"Decimal representation of {hex_num} is {hex_to_decimal(hex_num)}")
    except ValueError as e:
        print(e)
