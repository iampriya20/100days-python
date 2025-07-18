# day24_paragraph_analyzer.py

import re

def analyze_paragraph(text):
    words = len(text.split())
    sentences = len(re.findall(r'[.!?]', text))
    characters = len(text.replace(" ", ""))
    return words, sentences, characters

if __name__ == "__main__":
    print("📘 Enter your paragraph below (multi-line supported):\n")
    paragraph = ""
    while True:
        line = input()
        if not line:
            break
        paragraph += line + " "

    words, sentences, characters = analyze_paragraph(paragraph)

    print("\n📊 Analysis Report")
    print(f"🔠 Words: {words}")
    print(f"✍️ Sentences: {sentences}")
    print(f"🔤 Characters (no spaces): {characters}")
