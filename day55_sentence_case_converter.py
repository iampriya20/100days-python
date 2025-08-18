# Day 55: Sentence Case Converter

def sentence_case(text: str) -> str:
    """Return text with first character uppercase and the rest lowercase."""
    return text.capitalize()

if __name__ == "__main__":
    s = input("Enter text: ")
    print(sentence_case(s))
