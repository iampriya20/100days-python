# day22_remove_punctuation.py

import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

if __name__ == "__main__":
    user_input = input("Enter a sentence with punctuation: ")
    cleaned = remove_punctuation(user_input)
    print("Cleaned sentence:", cleaned)
