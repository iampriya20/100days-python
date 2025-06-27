# Day 4 - Vowel and Consonant Counter in a Sentence

# Take input from user
text = input("Enter a sentence: ")

# Define vowels
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

# Loop through each character
for char in text:
    if char.isalpha():  # Only count letters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print results
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
