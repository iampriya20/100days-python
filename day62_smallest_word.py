# Day 62: Find Smallest Word in a Sentence
import string

def smallest_word(sentence: str) -> str:
    # remove punctuation around words
    words = [w.strip(string.punctuation) for w in sentence.split()]
    words = [w for w in words if w]  # ignore empty strings
    return min(words, key=len) if words else ""

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    w = smallest_word(s)
    print("Smallest word:", w)
    print("Length:", len(w))
