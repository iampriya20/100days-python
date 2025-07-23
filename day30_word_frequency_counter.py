# day30_word_frequency_counter.py

text = input("Enter a sentence: ")

words = text.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\n📊 Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
