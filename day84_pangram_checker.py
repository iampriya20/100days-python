import string

def is_pangram(s: str) -> bool:
    letters = {ch.lower() for ch in s if ch.isalpha()}
    return set(string.ascii_lowercase).issubset(letters)

text = input("Enter a sentence: ")
print("Pangram" if is_pangram(text) else "Not a pangram")
