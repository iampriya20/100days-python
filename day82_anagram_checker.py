from collections import Counter

def normalize(s: str) -> str:
    # keep letters only, lowercase; ignore spaces/punctuation/numbers
    return "".join(ch.lower() for ch in s if ch.isalpha())

def is_anagram(a: str, b: str) -> bool:
    return Counter(normalize(a)) == Counter(normalize(b))

a = input("Enter first string: ")
b = input("Enter second string: ")
print("Anagram" if is_anagram(a, b) else "Not an anagram")
