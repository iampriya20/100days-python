# Day 92: Email Validator using Regex
import re

def is_valid_email(email: str) -> bool:
    """Validate an email address using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print(f"{email} is a valid email address ✅")
    else:
        print(f"{email} is not a valid email address ❌")
