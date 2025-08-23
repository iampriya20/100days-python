# Day 61: Find Largest Word in a Sentence
import string

def largest_word(sentence: str) -> str:
    # strip punctuation around words, then pick the first longest
    words = [w.strip(string.punctuation) for w in sentence.split()]
    words = [w for w in words if w]  # drop empties
    return max(words, key=len) if words else ""

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    w = largest_word(s)
    print("Largest word:", w)
    print("Length:", len(w))
