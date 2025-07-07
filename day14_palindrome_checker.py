# Day 14: Palindrome Checker (Simple Version)

text = input("Enter a word or phrase: ")
cleaned = text.lower().replace(" ", "")

reversed_text = ""
for char in cleaned:
    reversed_text = char + reversed_text

if cleaned == reversed_text:
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")