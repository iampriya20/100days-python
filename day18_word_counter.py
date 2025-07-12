# day18_word_counter.py

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display the result
print(f"The number of words in your sentence is: {word_count}")
