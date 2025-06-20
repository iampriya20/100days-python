# Day 4 - Word Reverser

# Ask user for input
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Reverse each word
reversed_words = [word[::-1] for word in words]

# Join back into a sentence
result = ' '.join(reversed_words)

print("Reversed sentence:", result)
