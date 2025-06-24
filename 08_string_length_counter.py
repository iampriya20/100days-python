# Day 8 - String Length Counter

text = input("Enter a word or sentence: ")

length_with_spaces = len(text)
length_without_spaces = len(text.replace(" ", ""))

print("\nString Length Analysis:")
print("Length (including spaces):", length_with_spaces)
print("Length (excluding spaces):", length_without_spaces)
