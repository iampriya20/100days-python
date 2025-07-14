# day21_password_strength_checker.py

import string

def check_password_strength(password):
    length = len(password) >= 8
    lowercase = any(char.islower() for char in password)
    uppercase = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in string.punctuation for char in password)

    if all([length, lowercase, uppercase, digit, special]):
        return "Strong"
    elif length and (lowercase or uppercase) and digit:
        return "Moderate"
    else:
        return "Weak"


if __name__ == "__main__":
    user_pass = input("Enter a password to check its strength: ")
    strength = check_password_strength(user_pass)
    print(f"Password Strength: {strength}")
