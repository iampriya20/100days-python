# day20_count_chars_digits_specials.py

def count_elements(text):
    letters = digits = specials = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():
            specials += 1

    return letters, digits, specials


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    letters, digits, specials = count_elements(user_input)
    
    print(f"Letters: {letters}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {specials}")
